
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

UNEMPLOYMENT_FILE = DATA / "unemployment.csv"


def clean_column_names(df):
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df


def main():
    
    unemployment = pd.read_csv(UNEMPLOYMENT_FILE)
    unemployment = clean_column_names(unemployment)

    required = {"state", "year", "value"}

    if not required.issubset(unemployment.columns):
        raise ValueError(
            f"unemployment.csv needs columns: {sorted(required)}"
        )

    unemployment["state"] = unemployment["state"].astype("string").str.strip()
    unemployment["year"] = pd.to_numeric(
        unemployment["year"], errors="coerce"
    )
    unemployment["value"] = pd.to_numeric(
        unemployment["value"], errors="coerce"
    )

    unemployment = unemployment.dropna(
        subset=["state", "year", "value"]
    )

    unemployment["year"] = unemployment["year"].astype(int)

    unemployment = unemployment[
        unemployment["indicator"].astype(str).str.contains(
            "Unemployment Rate", case=False, na=False
        )
    ].copy()

    duplicates = unemployment.duplicated(
        subset=["state", "year"], keep=False
    )

    if duplicates.any():
        raise ValueError(
            "Duplicate state-year records found. Check unemployment.csv."
        )

    unemployment.to_csv(
        OUT / "cleaned_unemployment.csv", index=False
    )

    latest_year = unemployment["year"].max()

    latest = unemployment[
        unemployment["year"] == latest_year
    ].sort_values("value", ascending=False)

    latest.to_csv(
        OUT / "state_unemployment_ranking.csv", index=False
    )

    plot_data = latest.head(15).sort_values("value")

    plt.figure(figsize=(10, 7))
    plt.barh(plot_data["state"], plot_data["value"])
    plt.xlabel("Youth unemployment rate (%)")
    plt.title(
        f"Youth Unemployment Rate by State/UT - {latest_year}"
    )
    plt.tight_layout()
    plt.savefig(
        OUT / "youth_unemployment_by_state.png", dpi=160
    )
    plt.close()

    yearly = (
        unemployment.groupby("year", as_index=False)["value"]
        .mean()
        .rename(columns={"value": "mean_state_unemployment_rate"})
    )

    yearly.to_csv(
        OUT / "yearly_unemployment_summary.csv", index=False
    )

    plt.figure(figsize=(9, 5))
    plt.plot(
        yearly["year"],
        yearly["mean_state_unemployment_rate"],
        marker="o"
    )
    plt.xlabel("Year")
    plt.ylabel("Mean state/UT unemployment rate (%)")
    plt.title("Youth Unemployment Rate Trends, 2022–2025")
    plt.xticks(yearly["year"])
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        OUT / "youth_unemployment_trend.png", dpi=160
    )
    plt.close()

    summary = [
        "YOUTH UNEMPLOYMENT ANALYSIS — INDIA",
        "Source: User-provided MoSPI eSankhyiki data",
        "Population: Ages 15–29, persons, rural + urban",
        f"Records after cleaning: {len(unemployment)}",
        f"States/UTs represented: {unemployment['state'].nunique()}",
        f"Years analysed: {int(unemployment['year'].min())}–{latest_year}",
        "",
        f"Highest rate in {latest_year}:",
        latest.head(5)[["state", "year", "value"]].to_string(index=False),
        "",
        f"Lowest rate in {latest_year}:",
        latest.tail(5).sort_values("value")[
            ["state", "year", "value"]
        ].to_string(index=False),
        "",
        "Mean of state/UT rates by year (not the official All India rate):",
        yearly.to_string(index=False),
        "",
        "Note: A simple average across states/UTs is not the same as the "
        "official national unemployment rate, because state populations "
        "and labour-force sizes differ.",
        "Migration data is not merged or correlated in this version."
    ]

    report = "\n".join(summary)
    (OUT / "analysis_summary.txt").write_text(
        report, encoding="utf-8"
    )

    print(report)
    print(f"\nDone. Results saved in: {OUT}")


if __name__ == "__main__":
    main()
