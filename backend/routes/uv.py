import os

import requests
from flask import Blueprint, jsonify, request

uv_bp = Blueprint("uv", __name__)

OPENWEATHER_URL = "https://api.openweathermap.org/data/3.0/onecall"


@uv_bp.route("/api/uv", methods=["GET"])
def get_uv():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if lat is None or lon is None:
        return jsonify({"error": "lat and lon are required"}), 400

    if not (-90 <= lat <= 90):
        return jsonify({"error": "Invalid latitude"}), 400

    if not (-180 <= lon <= 180):
        return jsonify({"error": "Invalid longitude"}), 400

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return jsonify({"error": "OPENWEATHER_API_KEY is not configured"}), 500

    try:
        response = requests.get(
            OPENWEATHER_URL,
            params={
                "lat": lat,
                "lon": lon,
                "exclude": "minutely,hourly,daily,alerts",
                "appid": api_key,
            },
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()

        uv_index = data.get("current", {}).get("uvi")
        if uv_index is None:
            return jsonify({"error": "UV data missing from provider response"}), 502

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

        return jsonify(
            {
                "uv_index": uv_index,
                "alert": alert,
                "source": "OpenWeather One Call 3.0",
            }
        )

    except requests.HTTPError:
        provider_message = None
        try:
            provider_message = response.json()
        except Exception:
            provider_message = response.text

        return (
            jsonify(
                {
                    "error": "Failed to fetch UV data from provider",
                    "provider_response": provider_message,
                }
            ),
            502,
        )
    except requests.RequestException as exc:
        return jsonify({"error": "Failed to fetch UV data", "details": str(exc)}), 502
