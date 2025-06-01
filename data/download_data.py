import os
import pandas as pd
import requests
from fredapi import Fred
from io import StringIO
import wbdata
import datetime
# from pandasdmx import Request

## LAYER 1 - CORE MACRO - RAW DATA -----------------------------------------------------------------------------------------------------------------

# --- US DATA ---

def download_us_data():
    print("🇺🇸 Downloading US macro data...")
    API_KEY = '10db6cf8e1187c3f55351905efa63817'
    DATA_PATH = 'data/Layer 1 - Core Macro/us/raw/'
    os.makedirs(DATA_PATH, exist_ok=True)

    fred = Fred(api_key=API_KEY)
    series = {
        'gdp_quarterly': 'GDP',
        'pce_consumption': 'PCEC96',
        'cpi_all_items': 'CPIAUCSL',
        'fed_funds_rate': 'FEDFUNDS',
        'yield_10y': 'GS10',
        'yield_2y': 'GS2',
        'unemployment_rate': 'UNRATE',
        'initial_jobless_claims': 'ICSA',
        'labor_force_participation': 'CIVPART'
    }

    for name, code in series.items():
        data = fred.get_series(code).to_frame(name)
        data.index.name = 'date'
        data.to_csv(f"{DATA_PATH}{name}.csv")

    spread = (fred.get_series('GS10') - fred.get_series('GS2')).to_frame(name='yield_curve_10y_2y')
    spread.index.name = 'date'
    spread.to_csv(f"{DATA_PATH}yield_curve_10y_2y.csv")

    print("✅ US macro raw data downloaded.\n")

# --- EURO AREA DATA ---

def download_euro_data():
    print("🇪🇺 Downloading Euro Area macro data...")
    DATA_PATH = 'data/Layer 1 - Core Macro/euro_area/raw/'
    os.makedirs(DATA_PATH, exist_ok=True)

    euro_series = {
        'euro_gdp_quarterly': "https://sdw.ecb.europa.eu/quickviewexport.do?SERIES_KEY=123.ESA.Q.I8.N.B1GQ.Y.A.V01.0000.Z.ZZZ.Z.Z.Z",
        'hicp_core': "https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_manr/default/table?lang=en",
        'ecb_refi_rate': "https://data.ecb.europa.eu/main-figures/ecb-interest-rates-and-exchange-rates/key-ecb-interest-rates",
        'unemployment_ea': "https://ec.europa.eu/eurostat/databrowser/view/une_rt_m/default/table?lang=en",
        'retail_sales_ea': "https://ec.europa.eu/eurostat/databrowser/view/STS_ROB_M/default/table?lang=en"
    }

    for name, url in euro_series.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(os.path.join(DATA_PATH, f"{name}.csv"), "wb") as f:
                    f.write(response.content)
                print(f"✔ Saved {name}.csv")
            else:
                print(f"❌ Failed to fetch {name}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error fetching {name}: {e}")

    print("✅ Euro Area macro data complete.\n")

# --- CHINA DATA ---

# --- CHINA DATA FROM WORLD BANK ---
def download_china_from_world_bank():
    print("🌍 Downloading China macro data from World Bank (direct API)...")
    DATA_PATH = 'data/Layer 1 - Core Macro/china/raw/'
    os.makedirs(DATA_PATH, exist_ok=True)

    indicators = {
        'china_gdp_usd': 'NY.GDP.MKTP.CD',
        'china_gdp_real_usd': 'NY.GDP.MKTP.KD',
        'china_cpi_inflation': 'FP.CPI.TOTL.ZG',
        'china_unemployment': 'SL.UEM.TOTL.ZS',
        'china_government_spending': 'NE.CON.GOVT.CD',
        'china_exports': 'NE.EXP.GNFS.CD',
        'china_imports': 'NE.IMP.GNFS.CD',
        'china_industrial_output': 'NV.IND.TOTL.CD',
        'china_labor_force_participation': 'SL.TLF.ACTI.ZS',
        'china_population': 'SP.POP.TOTL'
    }

    for name, code in indicators.items():
        url = f"https://api.worldbank.org/v2/country/CN/indicator/{code}?format=json&per_page=1000"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()[1]
                df = pd.DataFrame([
                    {'date': row['date'], name: row['value']}
                    for row in json_data if row['value'] is not None
                ])
                df['date'] = pd.to_datetime(df['date'])
                df.sort_values('date', inplace=True)
                df.to_csv(f"{DATA_PATH}{name}.csv", index=False)
                print(f"✔ Saved {name}.csv")
            else:
                print(f"❌ Failed to fetch {name}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error fetching {name}: {e}")


# --- CROSS COUNTRY DATA ---

# --- CROSS COUNTRY MACRO DATA ---
def download_cross_country_macro():
    print("🌐 Downloading cross-country macro data from World Bank...")
    DATA_PATH = 'data/Layer 1 - Core Macro/cross_country/raw/'
    os.makedirs(DATA_PATH, exist_ok=True)

    countries = {
        'US': 'USA',
        'EU': 'EMU',
        'CN': 'CHN'
    }

    indicators = {
        'gdp_growth': 'NY.GDP.MKTP.KD.ZG',
        'cpi_inflation': 'FP.CPI.TOTL.ZG',
        'unemployment_rate': 'SL.UEM.TOTL.ZS',
        'population': 'SP.POP.TOTL'
    }

    for var_name, ind_code in indicators.items():
        combined_df = pd.DataFrame()
        for label, iso in countries.items():
            url = f"https://api.worldbank.org/v2/country/{iso}/indicator/{ind_code}?format=json&per_page=1000"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    json_data = response.json()[1]
                    df = pd.DataFrame([
                        {'date': row['date'], label: row['value']}
                        for row in json_data if row['value'] is not None
                    ])
                    df['date'] = pd.to_datetime(df['date'])
                    df.set_index('date', inplace=True)
                    combined_df = combined_df.join(df, how='outer') if not combined_df.empty else df
                else:
                    print(f"❌ {label} - {var_name}: Failed ({response.status_code})")
            except Exception as e:
                print(f"❌ {label} - {var_name}: Error {e}")

        combined_df.sort_index(inplace=True)
        combined_df.to_csv(f"{DATA_PATH}cross_{var_name}.csv")
        print(f"✔ Saved cross_{var_name}.csv")

    print("✅ Cross-country macro data download complete.\n")
            

# --- RUN EVERYTHING ---
if __name__ == "__main__":
    download_us_data()
    download_euro_data()
    download_china_from_world_bank()
    # download_china_from_oecd()
    download_cross_country_macro()

## python data/download_data.py


## LAYER 2 - AI AUGMENTATION - RAW DATA -----------------------------------------------------------------------------------------------------------------

