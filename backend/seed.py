import pandas as pd
from database import engine, Base
from models import CancerRate, CancerRatio, UVSummary
from sqlalchemy.orm import sessionmaker

# Create all tables
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# ── Cancer Rates ──────────────────────────────────────────
print("Seeding cancer_rates...")
df = pd.read_csv("datasets/acimcombinedrates.csv")
df.columns = df.columns.str.strip()

for _, row in df.iterrows():
    record = CancerRate(
        year=int(row["Year"]) if pd.notna(row["Year"]) else None,
        sex=str(row["Sex"]) if pd.notna(row["Sex"]) else None,
        type=str(row["Type"]) if pd.notna(row["Type"]) else None,
        cancer_type=str(row["Cancer_Type"]) if pd.notna(row["Cancer_Type"]) else None,
        age_std_rate_aust=float(row["Age_Std_Rate_Aust"]) if pd.notna(row["Age_Std_Rate_Aust"]) else None,
        age_std_rate_segi=float(row["Age_Std_Rate_Segi"]) if pd.notna(row["Age_Std_Rate_Segi"]) else None,
        age_std_rate_who=float(row["Age_Std_Rate_WHO"]) if pd.notna(row["Age_Std_Rate_WHO"]) else None,
    )
    session.add(record)

session.commit()
print("cancer_rates done.")

# ── Cancer Ratios ─────────────────────────────────────────
print("Seeding cancer_ratios...")
df2 = pd.read_csv("datasets/acimcombinedratio.csv")
df2.columns = df2.columns.str.strip()

for _, row in df2.iterrows():
    record = CancerRatio(
        year=int(row["Year"]) if pd.notna(row["Year"]) else None,
        sex=str(row["Sex"]) if pd.notna(row["Sex"]) else None,
        cancer_type=str(row["Cancer_Type"]) if pd.notna(row["Cancer_Type"]) else None,
        aust_ratio=float(row["Aust_Mortality_to_incidence_ratio"]) if pd.notna(row["Aust_Mortality_to_incidence_ratio"]) else None,
        segi_ratio=float(row["Segi_Mortality_to_incidence_ratio"]) if pd.notna(row["Segi_Mortality_to_incidence_ratio"]) else None,
        who_ratio=float(row["WHO_Mortality_to_incidence_ratio"]) if pd.notna(row["WHO_Mortality_to_incidence_ratio"]) else None,
    )
    session.add(record)

session.commit()
print("cancer_ratios done.")

# ── UV Summary ────────────────────────────────────────────
print("Seeding uv_summary...")
df3 = pd.read_csv("datasets/DAILY_SUMMARY_all_cities.xls")
df3.columns = df3.columns.str.strip()

for _, row in df3.iterrows():
    record = UVSummary(
        city=str(row["city"]) if pd.notna(row["city"]) else None,
        generation=str(row["generation"]) if pd.notna(row["generation"]) else None,
        date=str(row["date"]) if pd.notna(row["date"]) else None,
        max_uv_index=float(row["max_uv_index"]) if pd.notna(row["max_uv_index"]) else None,
        avg_temperature=float(row["avg_temperature"]) if pd.notna(row["avg_temperature"]) else None,
    )
    session.add(record)

session.commit()
print("uv_summary done.")

session.close()
print("All done!")