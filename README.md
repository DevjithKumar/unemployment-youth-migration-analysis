# Unemployment and Youth Migration Analysis in India

## Project Overview
A Python-based data analysis project to explore youth unemployment rates and youth migration patterns across Indian states and Union Territories from 2015 to 2024.

## Technologies Used
- Python
- Pandas — data cleaning and analysis
- Matplotlib — data visualization
- CSV — data storage
- Git and GitHub — version control

## Project Workflow
1. Imported unemployment and migration datasets.
2. Cleaned and validated data using Pandas.
3. Handled missing values and duplicate records.
4. Generated state-wise rankings for the latest available year.
5. Analyzed the correlation between unemployment rates and migration counts.
6. Created charts and exported results for reporting.

## Project Structure

```text
unemployment-youth-migration-analysis/
├── data/
│   ├── unemployment.csv
│   ├── migration.csv
│   └── migration_template.csv
├── outputs/
│   ├── cleaned_unemployment.csv
│   ├── cleaned_migration.csv
│   ├── state_unemployment_ranking.csv
│   ├── state_migration_ranking.csv
│   ├── youth_unemployment_by_state.png
│   ├── youth_migration_by_state.png
│   └── analysis_summary.txt
├── main.py
├── requirements.txt
└── README.md
```

## Key Outputs
- Cleaned datasets
- State-wise unemployment and migration rankings
- Data visualization charts
- Correlation analysis
- Analysis summary report

## How to Run

Clone the repository:

```bash
git clone https://github.com/DevjithKumar/unemployment-youth-migration-analysis.git
cd unemployment-youth-migration-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

Results are saved in the `outputs/` directory.


## Author
**Devjith Kumar**

- GitHub: https://github.com/DevjithKumar
- LinkedIn: https://www.linkedin.com/in/r-devjith-kumar-95bb9b1b7/

