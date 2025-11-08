from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "city": "Sample City",
        "today_waste_tons": 15.2,
        "predicted_tomorrow_tons": round(random.uniform(14.5, 17.5), 1),
        "recycling_rate": 45,
        "daily": [8, 9, 10, 12, 13, 14, 15],
        "dates": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "bins": [
            {"id": "Bin 1", "lat": 40.7128, "lon": -74.0060, "fill_pct": 85},
            {"id": "Bin 2", "lat": 40.7158, "lon": -74.0020, "fill_pct": 60},
            {"id": "Bin 3", "lat": 40.7108, "lon": -74.0120, "fill_pct": 95}
        ]
    }
    return render_template("index.html", data=data)

@app.route('/api/data')
def api_data():
    data = {
        "predicted_tomorrow_tons": round(random.uniform(14.5, 17.5), 1)
    }
    return jsonify(data)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
