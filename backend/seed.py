from pathlib import Path

import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from database import Base, engine
from models import CancerRate, CancerRatio, UVSummary

BASE_DIR = Path(__file__).resolve().parent
DATASETS_DIR = BASE_DIR / "datasets"

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("Clearing existing data...")
    session.execute(text("TRUNCATE TABLE cancer_rates, cancer_ratios, uv_summary RESTART IDENTITY"))
    session.commit()

    print("Seeding cancer_rates...")
    df = pd.read_csv(DATASETS_DIR / "acimcombinedrates.csv")
    df.columns = df.columns.str.strip()

    for _, row in df.iterrows():
        session.add(
            CancerRate(
                year=int(row["Year"]) if pd.notna(row["Year"]) else None,
                sex=str(row["Sex"]) if pd.notna(row["Sex"]) else None,
                type=str(row["Type"]) if pd.notna(row["Type"]) else None,
                cancer_type=str(row["Cancer_Type"]) if pd.notna(row["Cancer_Type"]) else None,
                age_std_rate_aust=float(row["Age_Std_Rate_Aust"]) if pd.notna(row["Age_Std_Rate_Aust"]) else None,
                age_std_rate_segi=float(row["Age_Std_Rate_Segi"]) if pd.notna(row["Age_Std_Rate_Segi"]) else None,
                age_std_rate_who=float(row["Age_Std_Rate_WHO"]) if pd.notna(row["Age_Std_Rate_WHO"]) else None,
            )
        )
    session.commit()
    print("cancer_rates done.")

    print("Seeding cancer_ratios...")
    df2 = pd.read_csv(DATASETS_DIR / "acimcombinedratio.csv")
    df2.columns = df2.columns.str.strip()

    for _, row in df2.iterrows():
        session.add(
            CancerRatio(
                year=int(row["Year"]) if pd.notna(row["Year"]) else None,
                sex=str(row["Sex"]) if pd.notna(row["Sex"]) else None,
                cancer_type=str(row["Cancer_Type"]) if pd.notna(row["Cancer_Type"]) else None,
                aust_ratio=float(row["Aust_Mortality_to_incidence_ratio"])
                if pd.notna(row["Aust_Mortality_to_incidence_ratio"])
                else None,
                segi_ratio=float(row["Segi_Mortality_to_incidence_ratio"])
                if pd.notna(row["Segi_Mortality_to_incidence_ratio"])
                else None,
                who_ratio=float(row["WHO_Mortality_to_incidence_ratio"])
                if pd.notna(row["WHO_Mortality_to_incidence_ratio"])
                else None,
            )
        )
    session.commit()
    print("cancer_ratios done.")

    print("Seeding uv_summary...")
    df3 = pd.read_csv(DATASETS_DIR / "DAILY_SUMMARY_all_cities.xls")
    df3.columns = df3.columns.str.strip()

    for _, row in df3.iterrows():
        session.add(
            UVSummary(
                city=str(row["city"]) if pd.notna(row["city"]) else None,
                generation=str(row["generation"]) if pd.notna(row["generation"]) else None,
                date=str(row["date"]) if pd.notna(row["date"]) else None,
                max_uv_index=float(row["max_uv_index"]) if pd.notna(row["max_uv_index"]) else None,
                avg_temperature=float(row["avg_temperature"]) if pd.notna(row["avg_temperature"]) else None,
            )
        )
    session.commit()
    print("uv_summary done.")

    print("All done.")
finally:
    session.close()
