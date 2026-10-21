# Unemployment and Youth Migration Analysis in India

A Python-based data analysis project using **Pandas** and **Matplotlib** to clean official datasets, validate records, rank Indian states and union territories, and visualize youth unemployment and migration patterns.

## Project Overview

This project examines two related but distinct topics:

- **Youth unemployment:** State/UT-level unemployment rates for people aged 15–29 from 2022–2025.
- **Youth migration:** Census 2011 migration counts for people aged 15–29, aggregated by state/UT.

The two datasets cover different reference periods. The project analyses them separately and does not claim that historical migration counts explain recent unemployment trends.

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV data processing
- Data validation and visualization

## Data Sources

### 1. Youth Unemployment

**Source:** Ministry of Statistics and Programme Implementation (MoSPI), eSankhyiki.

The dataset contains annual youth unemployment rates for people aged 15–29, covering rural and urban sectors and the selected person-level and weekly-status filters.

- Period analysed: 2022–2025
- Geographic coverage: 36 states and union territories
- Measure: Unemployment rate (%)

### 2. Youth Migration

**Source:** Census of India 2011, D-05 — *Migrants by place of last residence, age, sex, reason for migration and duration of residence.*

Official dataset: https://censusindia.gov.in/nada/index.php/catalog/11030/study-description

The analysis selects ages 15–19, 20–24, and 25–29, then aggregates the migrant counts for each state/UT.

- Reference year: 2011
- Age range: 15–29 years
- Measure: Migrant count (persons)
- Selection: Total place of enumeration, total last residence, and all durations of residence
- Validation: 105 filtered records representing 35 state/UT entries across three age groups

**Why Census 2011?** It is the latest completed national Census providing the detailed migration table used in this project. The next Census is scheduled for 2027.

## Project Structure

```text
Unemplyment_youth_Migration_Analysis/
├── data/
│   ├── unemployment.csv
│   └── migration.csv
├── outputs/
│   ├── analysis_summary.txt
│   ├── cleaned_unemployment.csv
│   ├── state_unemployment_ranking.csv
│   ├── yearly_unemployment_summary.csv
│   ├── youth_unemployment_by_state.png
│   ├── youth_unemployment_trend.png
│   ├── cleaned_youth_migration_2011.csv
│   ├── state_youth_migration_2011.csv
│   ├── migration_analysis_summary.txt
│   └── youth_migration_top15.png
├── main.py
├── inspect_migration.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3
- Git (optional, for cloning the repository)

### Installation

Clone the repository and open its directory in VS Code.

```bash
git clone https://github.com/DevjithKumar/unemployment-youth-migration-analysis.git
cd unemployment-youth-migration-analysis
```

Create and activate a virtual environment on Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

### Run the analyses

Run the unemployment analysis:

```powershell
python main.py
```

Run the youth migration analysis:

```powershell
python inspect_migration.py
```

Generated CSV files, summary reports, and charts are saved in the `outputs/` directory.

## Key Findings

### Youth Unemployment

The simple, unweighted mean of state/UT unemployment rates declined from approximately **15.70% in 2022 to 13.73% in 2025**, with an increase in 2024.

This is an average across state/UT rates, not the official All-India unemployment rate. It does not account for differences in population or labour-force size.

### Youth Migration

Based on the selected Census 2011 data, Maharashtra has the highest aggregated youth migration count among the state/UT entries in this analysis, followed by Uttar Pradesh.

These are absolute counts, not population-adjusted migration rates. Larger populations can contribute to larger counts.

## Limitations

- Migration data is from Census 2011, while unemployment data covers 2022–2025.
- Migration counts include different reasons for migration and are not restricted to employment-related moves.
- Historical migration counts should not be interpreted as current migration levels.
- State/UT boundaries and administrative classifications may have changed since 2011.
- The analysis does not establish a causal relationship between unemployment and migration.
- The simple mean of state/UT unemployment rates is not the official national unemployment estimate.

## Future Improvements

- Analyse migration reasons, including work/employment and education.
- Add population-adjusted migration measures where suitable denominators are available.
- Improve geographic comparability across Census and recent datasets.
- Develop an interactive dashboard using Power BI or Streamlit.

## Author

**Devjith Kumar**

GitHub: https://github.com/DevjithKumar