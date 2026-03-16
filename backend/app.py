from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# Register route blueprints
from routes.uv import uv_bp
from routes.awareness import awareness_bp
from routes.prevention import prevention_bp

app.register_blueprint(uv_bp)
app.register_blueprint(awareness_bp)
app.register_blueprint(prevention_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)