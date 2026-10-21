
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path



DATA_FILE = Path("data/migration.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)



df = pd.read_csv(
    DATA_FILE,
    header=None,
    dtype=str,
    low_memory=False
)

print("Original dataset shape:", df.shape)

# Remove the title row and four header rows
df = df.iloc[5:].copy()



df = df[df[3].str.startswith("State -", na=False)].copy()

# Select:
# - Total place of enumeration
# - All durations of residence
# - Total last residence
# - Youth aged 15–29

age_groups = ["15-19", "20-24", "25-29"]

df = df[
    (df[4] == "Total")
    & (df[5] == "All durations of residence")
    & (df[7] == "Total")
    & (df[6].isin(age_groups))
].copy()


df["state"] = (
    df[3]
    .str.replace("State - ", "", regex=False)
    .str.replace(r"\s*\(\d+\)$", "", regex=True)
    .str.strip()
)

df["age_group"] = df[6].str.strip()

# Column 8 contains total migrants (Persons)
df["migrant_count"] = pd.to_numeric(
    df[8].str.replace(",", "", regex=False),
    errors="coerce"
)

# Remove rows with invalid migration counts
df = df.dropna(subset=["state", "migrant_count"])



print("\n--- DATA VALIDATION ---")
print("Filtered records:", len(df))
print("Unique states/UTs:", df["state"].nunique())

print("\nRecords per age group:")
print(df["age_group"].value_counts().sort_index().to_string())

if df.duplicated(subset=["state", "age_group"]).any():
    raise ValueError("Duplicate state and age-group records found.")

if set(df["age_group"].unique()) != set(age_groups):
    raise ValueError("One or more expected youth age groups are missing.")



cleaned_file = OUTPUT_DIR / "cleaned_youth_migration_2011.csv"

df[["state", "age_group", "migrant_count"]].to_csv(
    cleaned_file,
    index=False
)


youth_migration = (
    df.groupby("state", as_index=False)["migrant_count"]
    .sum()
    .sort_values("migrant_count", ascending=False)
)

ranking_file = OUTPUT_DIR / "state_youth_migration_2011.csv"

youth_migration.to_csv(
    ranking_file,
    index=False
)



print("\n--- TOP 10 STATES/UTs ---")
print(
    youth_migration.head(10).to_string(index=False)
)

print("\n--- BOTTOM 10 STATES/UTs ---")
print(
    youth_migration.tail(10)
    .sort_values("migrant_count")
    .to_string(index=False)
)


top15 = youth_migration.head(15).sort_values(
    "migrant_count",
    ascending=True
)

plt.figure(figsize=(11, 7))

plt.barh(
    top15["state"],
    top15["migrant_count"]
)

plt.title(
    "Top 15 States/UTs by Youth Migration Count (Census 2011)"
)
plt.xlabel("Migrants aged 15–29 (persons)")
plt.ylabel("State/UT")
plt.ticklabel_format(axis="x", style="plain")
plt.tight_layout()

chart_file = OUTPUT_DIR / "youth_migration_top15.png"

plt.savefig(
    chart_file,
    dpi=160,
    bbox_inches="tight"
)

plt.close()



summary_file = OUTPUT_DIR / "migration_analysis_summary.txt"

with open(summary_file, "w", encoding="utf-8") as file:
    file.write("YOUTH MIGRATION ANALYSIS - INDIA, CENSUS 2011\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Filtered records: {len(df)}\n")
    file.write(f"States/UTs represented: {youth_migration['state'].nunique()}\n")
    file.write("Age range: 15–29 years\n")
    file.write("Place of enumeration: Total\n")
    file.write("Last residence: Total\n")
    file.write("Duration: All durations of residence\n")
    file.write("Measure: Total migrants (Persons)\n\n")

    file.write("Top 10 states/UTs by youth migration count:\n")
    file.write(youth_migration.head(10).to_string(index=False))
    file.write("\n\n")

    file.write("Bottom 10 states/UTs by youth migration count:\n")
    file.write(
        youth_migration.tail(10)
        .sort_values("migrant_count")
        .to_string(index=False)
    )

    file.write(
        "\n\nLimitations:\n"
        "- Data is from the Census of India 2011.\n"
        "- Counts are not population-adjusted migration rates.\n"
        "- Migration is not restricted to employment-related moves.\n"
        "- These counts should not be directly correlated with "
        "unemployment figures from 2022–2025 as same-year data.\n"
    )



print("\n--- FILES SAVED ---")
print(cleaned_file)
print(ranking_file)
print(chart_file)
print(summary_file)

print("\nYouth migration analysis completed successfully.")
