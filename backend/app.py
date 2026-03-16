import os
import subprocess

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import inspect, text

from database import Base, SessionLocal, engine

# IMPORTANT: import models so SQLAlchemy registers all tables before create_all()
import models  # noqa: F401

from routes.awareness import awareness_bp
from routes.prevention import prevention_bp
from routes.uv import uv_bp

load_dotenv()

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

frontend_origins_raw = os.getenv(
    "FRONTEND_ORIGINS",
    "https://sunsmart-fullstack-1.onrender.com,http://localhost:5173",
)
frontend_origins = [origin.strip() for origin in frontend_origins_raw.split(",") if origin.strip()]

CORS(
    app,
    resources={r"/api/*": {"origins": frontend_origins}},
)

# This now works because models have been imported above
Base.metadata.create_all(bind=engine)


def seed_database_once():
    try:
        inspector = inspect(engine)
        existing_tables = set(inspector.get_table_names())

        required_tables = {"cancer_rates", "cancer_ratios", "uv_summary"}

        if not required_tables.issubset(existing_tables):
            print("Required tables missing. Running seed script...")
            subprocess.run(["python", "seed.py"], check=True)
            return

        db = SessionLocal()
        try:
            count = db.execute(text("SELECT COUNT(*) FROM cancer_rates")).scalar()
            if int(count or 0) == 0:
                print("Tables exist but database is empty. Running seed script...")
                subprocess.run(["python", "seed.py"], check=True)
            else:
                print("Database already seeded.")
        finally:
            db.close()

    except Exception as e:
        print("Seed check failed:", e)


seed_database_once()

app.register_blueprint(uv_bp)
app.register_blueprint(awareness_bp)
app.register_blueprint(prevention_bp)


@app.get("/")
def health():
    return jsonify(
        {
            "message": "SunSmart backend is running",
            "service": "backend",
            "status": "ok",
        }
    )


@app.get("/api/debug/db-status")
def debug_db_status():
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        db = SessionLocal()
        try:
            counts = {}
            for table_name in ["cancer_rates", "cancer_ratios", "uv_summary"]:
                if table_name in tables:
                    counts[table_name] = int(
                        db.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar() or 0
                    )
                else:
                    counts[table_name] = None
        finally:
            db.close()

        return jsonify(
            {
                "tables": tables,
                "row_counts": counts,
            }
        )
    except Exception as e:
        return jsonify({"error": "DB debug failed", "details": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
