from flask import Blueprint, jsonify, request
import requests
import os

uv_bp = Blueprint("uv", __name__)

@uv_bp.route("/api/uv")
def get_uv():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return jsonify({"error": "lat and lon are required"}), 400

    api_key = os.getenv("OPENWEATHER_API_KEY")

    res = requests.get(
        "https://api.openweathermap.org/data/3.0/onecall",
        params={
            "lat": lat,
            "lon": lon,
            "exclude": "minutely,hourly,daily,alerts",
            "appid": api_key
        }
    )

    if res.status_code != 200:
        return jsonify({"error": "Failed to fetch UV data"}), 500

    data = res.json()
    uv_index = data["current"]["uvi"]

    if uv_index <= 2:
        alert = "UV is low. Safe to be outdoors."
    elif uv_index <= 5:
        alert = "Moderate UV. Wear sunscreen SPF 30+."
    elif uv_index <= 7:
        alert = "High UV. Wear a hat and sunglasses."
    elif uv_index <= 10:
        alert = "Very high UV! Seek shade between 10am-4pm."
    else:
        alert = "Extreme UV! Avoid going outdoors if possible."

    return jsonify({
        "uv_index": uv_index,
        "alert": alert
    })