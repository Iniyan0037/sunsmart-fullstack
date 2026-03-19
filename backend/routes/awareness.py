from flask import Blueprint, jsonify, request
from sqlalchemy import text
from database import engine

awareness_bp = Blueprint("awareness", __name__)


# -----------------------------
# Helper: safe float conversion
# -----------------------------
def safe_float(value):
    try:
        if value is None:
            return None
        return float(value)
    except:
        return None


# ---------------------------------------
# GET /api/cancer-stats  (FIXED VERSION)
# ---------------------------------------
@awareness_bp.route("/api/cancer-stats", methods=["GET"])
def get_cancer_stats():
    try:
        with engine.connect() as db:
            result = db.execute(text("""
                SELECT 
                    year, 
                    sex, 
                    AVG(age_std_rate_aust) as age_std_rate_aust
                FROM cancer_rates
                WHERE cancer_type = 'Melanoma of the skin'
                AND age_std_rate_aust IS NOT NULL
                AND sex IN ('Male', 'Female')
                GROUP BY year, sex
                ORDER BY year ASC
            """)).fetchall()

        male_data = {}
        female_data = {}

        for row in result:
            year = row[0]
            sex = row[1]
            value = safe_float(row[2])

            if value is None:
                continue

            if sex == "Male":
                male_data[year] = value
            elif sex == "Female":
                female_data[year] = value

        # Get sorted years
        years = sorted(set(male_data.keys()) | set(female_data.keys()))

        male_values = [male_data.get(year, None) for year in years]
        female_values = [female_data.get(year, None) for year in years]

        return jsonify({
            "years": years,
            "male": male_values,
            "female": female_values
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------------------
# GET /api/uv-trends
# ---------------------------------------
@awareness_bp.route("/api/uv-trends", methods=["GET"])
def get_uv_trends():
    city = request.args.get("city", "Melbourne")

    try:
        with engine.connect() as db:
            result = db.execute(text("""
                SELECT year, avg_temp
                FROM uv_summary
                WHERE city = :city
                AND avg_temp IS NOT NULL
                ORDER BY year ASC
            """), {"city": city}).fetchall()

        years = []
        temps = []

        for row in result:
            year = row[0]
            temp = safe_float(row[1])

            if temp is None:
                continue

            years.append(year)
            temps.append(temp)

        return jsonify({
            "city": city,
            "years": years,
            "temps": temps
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
