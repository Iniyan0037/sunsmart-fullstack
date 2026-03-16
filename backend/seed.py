from pathlib import Path

import pandas as pd
from sqlalchemy.orm import sessionmaker

from database import Base, engine
from models import CancerRate, CancerRatio, UVSummary

BASE_DIR = Path(__file__).resolve().parent
DATASETS_DIR = BASE_DIR / "datasets"

Session = sessionmaker(bind=engine)


def _none_if_nan(value):
    if pd.isna(value):
        return None
    return value


def seed_database():
    Base.metadata.create_all(bind=engine)

    session = Session()
    try:
        session.query(CancerRate).delete()
        session.query(CancerRatio).delete()
        session.query(UVSummary).delete()
        session.commit()

        cancer_rates_df = pd.read_csv(DATASETS_DIR / "acimcombinedrates.csv")
        cancer_rates_df.columns = cancer_rates_df.columns.str.strip()

        cancer_rates_rows = []
        for _, row in cancer_rates_df.iterrows():
            cancer_rates_rows.append(
                {
                    "year": int(row["Year"]) if pd.notna(row["Year"]) else None,
                    "sex": str(row["Sex"]) if pd.notna(row["Sex"]) else None,
                    "type": str(row["Type"]) if pd.notna(row["Type"]) else None,
                    "cancer_type": str(row["Cancer_Type"]) if pd.notna(row["Cancer_Type"]) else None,
                    "age_std_rate_aust": float(row["Age_Std_Rate_Aust"]) if pd.notna(row["Age_Std_Rate_Aust"]) else None,
                    "age_std_rate_segi": float(row["Age_Std_Rate_Segi"]) if pd.notna(row["Age_Std_Rate_Segi"]) else None,
                    "age_std_rate_who": float(row["Age_Std_Rate_WHO"]) if pd.notna(row["Age_Std_Rate_WHO"]) else None,
                }
            )

        session.bulk_insert_mappings(CancerRate, cancer_rates_rows)
        session.commit()

        cancer_ratio_df = pd.read_csv(DATASETS_DIR / "acimcombinedratio.csv")
        cancer_ratio_df.columns = cancer_ratio_df.columns.str.strip()

        cancer_ratio_rows = []
        for _, row in cancer_ratio_df.iterrows():
            cancer_ratio_rows.append(
                {
                    "year": int(row["Year"]) if pd.notna(row["Year"]) else None,
                    "sex": str(row["Sex"]) if pd.notna(row["Sex"]) else None,
                    "cancer_type": str(row["Cancer_Type"]) if pd.notna(row["Cancer_Type"]) else None,
                    "aust_ratio": float(row["Aust_Mortality_to_incidence_ratio"])
                    if pd.notna(row["Aust_Mortality_to_incidence_ratio"])
                    else None,
                    "segi_ratio": float(row["Segi_Mortality_to_incidence_ratio"])
                    if pd.notna(row["Segi_Mortality_to_incidence_ratio"])
                    else None,
                    "who_ratio": float(row["WHO_Mortality_to_incidence_ratio"])
                    if pd.notna(row["WHO_Mortality_to_incidence_ratio"])
                    else None,
                }
            )

        session.bulk_insert_mappings(CancerRatio, cancer_ratio_rows)
        session.commit()

        # This file is CSV-formatted even though the extension is .xls
        uv_summary_df = pd.read_csv(DATASETS_DIR / "DAILY_SUMMARY_all_cities.xls")
        uv_summary_df.columns = uv_summary_df.columns.str.strip()

        uv_summary_rows = []
        for _, row in uv_summary_df.iterrows():
            uv_summary_rows.append(
                {
                    "city": str(row["city"]) if pd.notna(row["city"]) else None,
                    "generation": str(row["generation"]) if pd.notna(row["generation"]) else None,
                    "date": str(row["date"]) if pd.notna(row["date"]) else None,
                    "max_uv_index": float(row["max_uv_index"]) if pd.notna(row["max_uv_index"]) else None,
                    "avg_temperature": float(row["avg_temperature"]) if pd.notna(row["avg_temperature"]) else None,
                }
            )

        session.bulk_insert_mappings(UVSummary, uv_summary_rows)
        session.commit()

        return {
            "cancer_rates_rows": len(cancer_rates_rows),
            "cancer_ratios_rows": len(cancer_ratio_rows),
            "uv_summary_rows": len(uv_summary_rows),
        }

    finally:
        session.close()


if __name__ == "__main__":
    result = seed_database()
    print(result)
