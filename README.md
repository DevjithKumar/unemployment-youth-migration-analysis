# Unemployment and Youth Migration Analysis in India

A Python data-analysis project using Pandas and Matplotlib for cleaning, state-level comparison, rankings, and chart generation.

## Quick start (Windows + VS Code)

1. Open this folder in VS Code.
2. Open Terminal → New Terminal.
3. Run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py main.py
```

If PowerShell blocks activation, run `py -m pip install -r requirements.txt` and then `py main.py` without activating the environment.

The script will run immediately using clearly labelled DEMO DATA if official CSVs are not present. Do not report demo results as real findings.

## Replace demo data with real data

Put two files inside `data/` with these exact names:

### `unemployment.csv`
Required columns:
- `state` — state/UT name
- `year` — reference year
- `youth_unemployment_rate` — rate in percent for the chosen youth age group

Official source to start from:
- Open Government Data (India), state/UT unemployment rate for persons aged 15–29, PLFS 2019–20 to 2023–24: https://www.data.gov.in/keywords/plfs
- PLFS annual reports: https://dge.gov.in/reference-publication-reports-annual

### `migration.csv`
Required columns:
- `state` — state/UT name
- `year` — migration reference year
- `youth_migrants` — migrant count for a clearly defined youth age group and migration definition

Official source to start from:
- Census of India, D-05: migrants by last residence, age, sex and duration, 2011: https://censusindia.gov.in/nada/index.php/catalog/11030/study-description
- Census of India, D-03: migrants by last residence, duration and reason, 2011: https://censusindia.gov.in/nada/index.php/catalog/10840/study-description

Download the official tables and prepare the two CSVs using consistent state names. Do not combine all-age migration counts with youth unemployment and call it a youth-to-youth comparison. The project keeps reference years visible because PLFS and Census periods may differ.

## Outputs
The `outputs/` folder will contain:
- cleaned CSV files
- state ranking CSVs
- unemployment and migration bar charts (PNG)
- a text summary

## Suggested next improvements
1. Align migration and unemployment data by state/UT and compatible time period.
2. Add age-group and migration-reason filters when the source supports them.
3. Add correlation only when the measures are comparable and explain that correlation does not establish causation.
4. Add a Streamlit dashboard after validating the data.
