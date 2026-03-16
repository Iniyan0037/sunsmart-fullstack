from flask import Blueprint, jsonify, request

prevention_bp = Blueprint("prevention", __name__)

@prevention_bp.route("/api/sunscreen")
def sunscreen():
    try:
        uv = float(request.args.get("uv", 0))
    except ValueError:
        return jsonify({"error": "Invalid UV value"}), 400

    if uv <= 2:
        spf = "SPF 15+"
        face = 0.5
        body = 3
        reapply = 120
        note = "Low UV. Sunscreen optional but recommended."
    elif uv <= 5:
        spf = "SPF 30+"
        face = 1
        body = 5
        reapply = 90
        note = "Moderate UV. Apply before going outdoors."
    elif uv <= 7:
        spf = "SPF 30+"
        face = 1.5
        body = 7
        reapply = 60
        note = "High UV. Apply generously and reapply regularly."
    elif uv <= 10:
        spf = "SPF 50+"
        face = 2
        body = 9
        reapply = 60
        note = "Very high UV. Reapply every hour if sweating."
    else:
        spf = "SPF 50+"
        face = 2.5
        body = 10
        reapply = 45
        note = "Extreme UV. Maximum protection required."

    return jsonify({
        "uv_index": uv,
        "recommended_spf": spf,
        "face_teaspoons": face,
        "body_teaspoons": body,
        "reapply_minutes": reapply,
        "note": note
    })


@prevention_bp.route("/api/clothing")
def clothing():
    try:
        uv = float(request.args.get("uv", 0))
    except ValueError:
        return jsonify({"error": "Invalid UV value"}), 400

    if uv <= 2:
        items = ["Light shirt", "Optional sunglasses"]
        note = "Low UV. Standard clothing is fine."
    elif uv <= 5:
        items = ["Shirt with collar", "Sunglasses", "Sunscreen on exposed skin"]
        note = "Moderate UV. Cover up during peak hours."
    elif uv <= 7:
        items = ["Long-sleeve shirt (UPF 30+)", "Wide-brim hat", "Sunglasses", "Sunscreen"]
        note = "High UV. Cover as much skin as possible."
    elif uv <= 10:
        items = ["Long-sleeve shirt (UPF 50+)", "Wide-brim hat", "Wraparound sunglasses", "Sunscreen SPF 50+", "Seek shade"]
        note = "Very high UV. Avoid being outdoors 10am-4pm."
    else:
        items = ["Full coverage clothing (UPF 50+)", "Wide-brim hat", "Wraparound sunglasses", "Sunscreen SPF 50+", "Stay indoors if possible"]
        note = "Extreme UV. Minimise all outdoor exposure."

    return jsonify({
        "uv_index": uv,
        "items": items,
        "note": note
    })