
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

UNEMPLOYMENT_FILE = DATA / "unemployment.csv"
MIGRATION_FILE = DATA / "migration.csv"


def load_data():
    unemployment = pd.read_csv(UNEMPLOYMENT_FILE)
    migration = pd.read_csv(MIGRATION_FILE)
    print("Using CSV files found in data/.")
    return unemployment, migration


def clean_column_names(df):
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df


def main():
    unemployment, migration = load_data()
    unemployment = clean_column_names(unemployment)
    migration = clean_column_names(migration)

    required_u = {"state", "year", "youth_unemployment_rate"}
    required_m = {"state", "year", "youth_migrants"}

    if not required_u.issubset(unemployment.columns):
        raise ValueError(f"unemployment.csv needs columns: {sorted(required_u)}")
    if not required_m.issubset(migration.columns):
        raise ValueError(f"migration.csv needs columns: {sorted(required_m)}")

    for df in (unemployment, migration):
        df["state"] = df["state"].astype(str).str.strip().str.title()
        df["year"] = pd.to_numeric(df["year"], errors="coerce")

    unemployment["youth_unemployment_rate"] = pd.to_numeric(
        unemployment["youth_unemployment_rate"], errors="coerce"
    )
    migration["youth_migrants"] = pd.to_numeric(
        migration["youth_migrants"], errors="coerce"
    )

    unemployment = unemployment.dropna(
        subset=["state", "year", "youth_unemployment_rate"]
    ).drop_duplicates()

    migration = migration.dropna(
        subset=["state", "year", "youth_migrants"]
    ).drop_duplicates()

    unemployment.to_csv(OUT / "cleaned_unemployment.csv", index=False)
    migration.to_csv(OUT / "cleaned_migration.csv", index=False)

    latest_u_year = unemployment["year"].max()
    latest_m_year = migration["year"].max()

    latest_u = unemployment[
        unemployment["year"] == latest_u_year
    ].sort_values("youth_unemployment_rate", ascending=False)

    latest_m = migration[
        migration["year"] == latest_m_year
    ].sort_values("youth_migrants", ascending=False)

    latest_u.to_csv(OUT / "state_unemployment_ranking.csv", index=False)
    latest_m.to_csv(OUT / "state_migration_ranking.csv", index=False)

    plot_u = latest_u.head(15).sort_values("youth_unemployment_rate")
    plt.figure(figsize=(10, 6))
    plt.barh(plot_u["state"], plot_u["youth_unemployment_rate"])
    plt.xlabel("Youth unemployment rate (%)")
    plt.title(f"Youth unemployment by state/UT - {int(latest_u_year)}")
    plt.tight_layout()
    plt.savefig(OUT / "youth_unemployment_by_state.png", dpi=160)
    plt.close()

    plot_m = latest_m.head(15).sort_values("youth_migrants")
    plt.figure(figsize=(10, 6))
    plt.barh(plot_m["state"], plot_m["youth_migrants"])
    plt.xlabel("Youth migrants (people)")
    plt.title(f"Youth migration by state/UT - {int(latest_m_year)}")
    plt.tight_layout()
    plt.savefig(OUT / "youth_migration_by_state.png", dpi=160)
    plt.close()

    combined = pd.merge(
        unemployment,
        migration,
        on=["state", "year"],
        how="inner"
    )

    correlation = combined["youth_unemployment_rate"].corr(
        combined["youth_migrants"]
    )

    summary = [
        "UNEMPLOYMENT & YOUTH MIGRATION ANALYSIS",
        "Mode: USER-PROVIDED CSV DATA",
        f"Unemployment rows after cleaning: {len(unemployment)}",
        f"Migration rows after cleaning: {len(migration)}",
        f"Unemployment reference year analysed: {int(latest_u_year)}",
        f"Migration reference year analysed: {int(latest_m_year)}",
        f"Matched state-year records: {len(combined)}",
        f"Correlation between unemployment rate and migrant count: {correlation:.2f}",
        "",
        "Top states/UTs by youth unemployment rate:",
        latest_u.head(5).to_string(index=False),
        "",
        "Top states/UTs by youth migrant count:",
        latest_m.head(5).to_string(index=False),
        "",
       
    ]

    report = "\n".join(summary)
    (OUT / "analysis_summary.txt").write_text(report, encoding="utf-8")

    print(report)
    print(f"\nDone. Results saved in: {OUT}")


if __name__ == "__main__":
    main()
