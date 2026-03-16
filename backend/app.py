import os
import subprocess

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

from database import Base, engine
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

# create database tables
Base.metadata.create_all(bind=engine)

# register routes
app.register_blueprint(uv_bp)
app.register_blueprint(awareness_bp)
app.register_blueprint(prevention_bp)


# ---------- AUTO SEED DATABASE ----------
def seed_database_once():
    try:
        from sqlalchemy import text
        from database import SessionLocal

        db = SessionLocal()

        result = db.execute(text("SELECT COUNT(*) FROM cancer_rates")).scalar()

        db.close()

        # if table empty → seed database
        if result == 0:
            print("Database empty. Running seed script...")
            subprocess.run(["python", "seed.py"], check=True)
        else:
            print("Database already seeded.")

    except Exception as e:
        print("Seed check failed:", e)


seed_database_once()
# ---------------------------------------


@app.get("/")
def health():
    return jsonify(
        {
            "message": "SunSmart backend is running",
            "service": "backend",
            "status": "ok",
        }
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
