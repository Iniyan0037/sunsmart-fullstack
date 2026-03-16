import math

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from database import SessionLocal

awareness_bp = Blueprint("awareness", __name__)


@awareness_bp.route("/api/cancer-stats", methods=["GET"])
def cancer_stats():
    db = SessionLocal()
    try:
        result = db.execute(
            text(
                """
                SELECT year, sex, age_std_rate_aust
                FROM cancer_rates
                WHERE cancer_type = 'Melanoma of the skin'
                  AND age_std_rate_aust IS NOT NULL
                  AND sex IN ('Male', 'Female')
                ORDER BY year ASC
                """
            )
        ).mappings().all()

        male_data = {}
        female_data = {}

        for row in result:
            year = row["year"]
            sex = row["sex"]
            rate = row["age_std_rate_aust"]

            if year is None or sex is None or rate is None:
                continue

            try:
                rate_value = float(rate)
            except (TypeError, ValueError):
                continue

            if math.isnan(rate_value) or math.isinf(rate_value):
                continue

            if sex == "Male":
                male_data[int(year)] = round(rate_value, 2)
            elif sex == "Female":
                female_data[int(year)] = round(rate_value, 2)

        years = sorted(set(male_data.keys()) | set(female_data.keys()))

        return jsonify(
            {
                "labels": years,
                "datasets": [
                    {
                        "label": "Male",
                        "data": [male_data.get(y, None) for y in years],
                        "borderColor": "#3498db",
                        "backgroundColor": "rgba(52,152,219,0.2)",
                    },
                    {
                        "label": "Female",
                        "data": [female_data.get(y, None) for y in years],
                        "borderColor": "#e74c3c",
                        "backgroundColor": "rgba(231,76,60,0.2)",
                    },
                ],
            }
        )
    finally:
        db.close()


@awareness_bp.route("/api/uv-trends", methods=["GET"])
def uv_trends():
    city = request.args.get("city", "Melbourne")

    db = SessionLocal()
    try:
        result = db.execute(
            text(
                """
                SELECT
                    EXTRACT(YEAR FROM date::date) AS year,
                    ROUND(AVG(avg_temperature)::numeric, 2) AS avg_temp
                FROM uv_summary
                WHERE city = :city
                  AND avg_temperature IS NOT NULL
                GROUP BY year
                ORDER BY year ASC
                """
            ),
            {"city": city},
        ).mappings().all()

        years = []
        temps = []

        for row in result:
            year = row["year"]
            avg_temp = row["avg_temp"]

            if year is None or avg_temp is None:
                continue

            try:
                temp_value = float(avg_temp)
            except (TypeError, ValueError):
                continue

            if math.isnan(temp_value) or math.isinf(temp_value):
                continue

            years.append(int(year))
            temps.append(temp_value)

        cities_result = db.execute(
            text("SELECT DISTINCT city FROM uv_summary WHERE city IS NOT NULL ORDER BY city")
        ).mappings().all()
        cities = [row["city"] for row in cities_result]

        return jsonify(
            {
                "city": city,
                "cities": cities,
                "labels": years,
                "datasets": [
                    {
                        "label": f"Avg Temperature - {city}",
                        "data": temps,
                        "borderColor": "#e67e22",
                        "backgroundColor": "rgba(230,126,34,0.2)",
                    }
                ],
            }
        )
    finally:
        db.close()
