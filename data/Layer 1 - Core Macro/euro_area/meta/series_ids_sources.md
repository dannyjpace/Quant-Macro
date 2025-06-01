#  Euro Area Macroeconomic Raw Data — Metadata

This file documents the raw macroeconomic series collected for the Euro Area (EA19), including dataset IDs, sources, and key notes.

---

###  Dataset Identifiers & Sources

| File Name              | Dataset / Series ID                | Source                                                                 |
|------------------------|-------------------------------------|------------------------------------------------------------------------|
| euro_gdp_quarterly.csv | `namq_10_gdp` (Eurostat)           | [Link](https://ec.europa.eu/eurostat/databrowser/view/namq_10_gdp/default/table?lang=en) |
| hicp_core.csv          | `prc_hicp_manr` (Eurostat)         | [Link](https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_manr/default/table?lang=en) |
| unemployment_ea.csv    | `une_rt_m` (Eurostat)              | [Link](https://ec.europa.eu/eurostat/databrowser/view/une_rt_m/default/table?lang=en)     |
| retail_sales_ea.csv    | `sts_trtu_m` (Eurostat)            | [Link](https://ec.europa.eu/eurostat/databrowser/view/STS_ROB_M/default/table?lang=en)    |
| ecb_refi_rate.csv      | `FM.M.IRF.MEUR.STN.RATE` (ECB SDW) | [Link](https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=143.FM.M.IRF.MEUR.STN.RATE)      |

---

###  Variable Details

| File Name              | Description                                      | Frequency | Units / Notes             |
|------------------------|--------------------------------------------------|-----------|----------------------------|
| euro_gdp_quarterly.csv | Real GDP (CLV10_MEUR, seasonally adjusted)       | Quarterly | Billion EUR                |
| hicp_core.csv          | Harmonised Index of Consumer Prices (Core)       | Monthly   | YoY % change               |
| unemployment_ea.csv    | Unemployment Rate (seasonally adjusted)          | Monthly   | % of active population     |
| retail_sales_ea.csv    | Retail Trade Index (volume, seasonally adjusted) | Monthly   | Index (2015 = 100)         |
| ecb_refi_rate.csv      | Main Refinancing Operations Rate (Fixed Tender)  | Monthly   | % interest rate            |


Note: `ecb_refi_rate.csv` was manually downloaded from ECB SDW Quickview export.
