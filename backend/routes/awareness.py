from flask import Blueprint, jsonify, request
from database import SessionLocal
from sqlalchemy import text

awareness_bp = Blueprint("awareness", __name__)

@awareness_bp.route("/api/cancer-stats")
def cancer_stats():
    db = SessionLocal()
    try:
        # Melanoma incidence rates over time, both sexes
        result = db.execute(text("""
            SELECT year, sex, age_std_rate_aust
            FROM cancer_rates
            WHERE cancer_type = 'Melanoma of the skin'
            AND age_std_rate_aust IS NOT NULL
            AND sex IN ('Male', 'Female')
            ORDER BY year ASC
        """)).fetchall()

        male_data = {}
        female_data = {}

        for row in result:
            if row.sex == 'Male':
                male_data[row.year] = round(float(row.age_std_rate_aust), 2)
            elif row.sex == 'Female':
                female_data[row.year] = round(float(row.age_std_rate_aust), 2)

        years = sorted(set(male_data.keys()) | set(female_data.keys()))

        return jsonify({
            "labels": years,
            "datasets": [
                {
                    "label": "Male",
                    "data": [male_data.get(y) for y in years],
                    "borderColor": "#3498db",
                    "backgroundColor": "rgba(52,152,219,0.2)"
                },
                {
                    "label": "Female",
                    "data": [female_data.get(y) for y in years],
                    "borderColor": "#e74c3c",
                    "backgroundColor": "rgba(231,76,60,0.2)"
                }
            ]
        })
    finally:
        db.close()


@awareness_bp.route("/api/uv-trends")
def uv_trends():
    city = request.args.get("city", "Melbourne")
    db = SessionLocal()
    try:
        result = db.execute(text("""
            SELECT
                EXTRACT(YEAR FROM date::date) AS year,
                ROUND(AVG(avg_temperature)::numeric, 2) AS avg_temp
            FROM uv_summary
            WHERE city = :city
            AND avg_temperature IS NOT NULL
            GROUP BY year
            ORDER BY year ASC
        """), {"city": city}).fetchall()

        years = [int(row.year) for row in result]
        temps = [float(row.avg_temp) for row in result]

        # Available cities for frontend dropdown
        cities_result = db.execute(text(
            "SELECT DISTINCT city FROM uv_summary ORDER BY city"
        )).fetchall()
        cities = [row.city for row in cities_result]

        return jsonify({
            "city": city,
            "cities": cities,
            "labels": years,
            "datasets": [
                {
                    "label": f"Avg Temperature - {city}",
                    "data": temps,
                    "borderColor": "#e67e22",
                    "backgroundColor": "rgba(230,126,34,0.2)"
                }
            ]
        })
    finally:
        db.close()