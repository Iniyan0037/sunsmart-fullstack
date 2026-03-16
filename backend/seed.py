from pathlib import Path

import pandas as pd
from sqlalchemy.orm import sessionmaker

from database import Base, engine
from models import CancerRate, CancerRatio, UVSummary

BASE_DIR = Path(__file__).resolve().parent
DATASETS_DIR = BASE_DIR / "datasets"

Session = sessionmaker(bind=engine)


def seed_database():
    Base.metadata.create_all(bind=engine)

    session = Session()
    try:
        session.query(CancerRate).delete()
        session.query(CancerRatio).delete()
        session.query(UVSummary).delete()
        session.commit()

        df = pd.read_csv(DATASETS_DIR / "acimcombinedrates.csv")
        df.columns = df.columns.str.strip()

        cancer_rates = []
        for _, row in df.iterrows():
            cancer_rates.append(
                {
                    "year": int(row["Year"]) if pd.notna(row["Year"]) else None,
                    "sex": row["Sex"],
                    "type": row["Type"],
                    "cancer_type": row["Cancer_Type"],
                    "age_std_rate_aust": row["Age_Std_Rate_Aust"],
                    "age_std_rate_segi": row["Age_Std_Rate_Segi"],
                    "age_std_rate_who": row["Age_Std_Rate_WHO"],
                }
            )

        session.bulk_insert_mappings(CancerRate, cancer_rates)
        session.commit()

        df = pd.read_csv(DATASETS_DIR / "acimcombinedratio.csv")
        df.columns = df.columns.str.strip()

        cancer_ratios = []
        for _, row in df.iterrows():
            cancer_ratios.append(
                {
                    "year": row["Year"],
                    "sex": row["Sex"],
                    "cancer_type": row["Cancer_Type"],
                    "aust_ratio": row["Aust_Mortality_to_incidence_ratio"],
                    "segi_ratio": row["Segi_Mortality_to_incidence_ratio"],
                    "who_ratio": row["WHO_Mortality_to_incidence_ratio"],
                }
            )

        session.bulk_insert_mappings(CancerRatio, cancer_ratios)
        session.commit()

        df = pd.read_csv(DATASETS_DIR / "DAILY_SUMMARY_all_cities.xls")
        df.columns = df.columns.str.strip()

        uv_rows = []
        for _, row in df.iterrows():
            uv_rows.append(
                {
                    "city": row["city"],
                    "generation": row["generation"],
                    "date": row["date"],
                    "max_uv_index": row["max_uv_index"],
                    "avg_temperature": row["avg_temperature"],
                }
            )

        session.bulk_insert_mappings(UVSummary, uv_rows)
        session.commit()

        return {
            "cancer_rates": len(cancer_rates),
            "cancer_ratios": len(cancer_ratios),
            "uv_summary": len(uv_rows),
        }

    finally:
        session.close()


if __name__ == "__main__":
    print("Seeding database...")
    result = seed_database()
    print("Seed complete:", result)
