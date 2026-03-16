import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import inspect, text

from database import Base, SessionLocal, engine

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

Base.metadata.create_all(bind=engine)

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
