# 🌐 Cross-Country Macroeconomic Raw Data — Metadata

This file documents the macroeconomic series downloaded from the World Bank API across the United States (USA), Euro Area (EMU), and China (CHN), saved under `cross_country/raw/`.

All indicators are annual and aligned by date to facilitate global comparisons in forecasting and allocation models.

---

###  Included Datasets

| File Name                  | World Bank Indicator Code | Description                                 | Frequency | Units / Notes             |
|----------------------------|----------------------------|---------------------------------------------|-----------|----------------------------|
| cross_gdp_growth.csv       | `NY.GDP.MKTP.KD.ZG`        | Real GDP growth rate (% change)             | Annual    | Percent                    |
| cross_cpi_inflation.csv    | `FP.CPI.TOTL.ZG`           | Consumer Price Index (YoY inflation)        | Annual    | Percent                    |
| cross_unemployment_rate.csv| `SL.UEM.TOTL.ZS`           | Unemployment rate                           | Annual    | Percent of labor force     |
| cross_population.csv       | `SP.POP.TOTL`              | Total population                            | Annual    | Number of people           |

---

###  ISO Country Codes

| Label | Country        | World Bank Code |
|-------|----------------|-----------------|
| US    | United States  | USA             |
| EU    | Euro Area      | EMU             |
| CN    | China          | CHN             |

---

**Source**: [World Bank Open Data API](https://data.worldbank.org/indicator)
