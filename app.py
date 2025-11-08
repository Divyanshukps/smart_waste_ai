from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        city = request.form["city"]
        population = float(request.form["population"])
        avg_waste = float(request.form["avg_waste"])  # tons per day
        recycling_rate = float(request.form["recycling_rate"])

        # --- Prediction Logic (AI-like demo) ---
        predicted_tomorrow = round(avg_waste * random.uniform(1.01, 1.15), 2)
        weekly_total = round(predicted_tomorrow * 7, 2)
        monthly_total = round(predicted_tomorrow * 30, 2)
        recyclable = round(monthly_total * (recycling_rate / 100), 2)
        landfill = round(monthly_total - recyclable, 2)
        carbon_emission = round(monthly_total * 0.25, 2)
        trucks_needed = round(monthly_total / 5, 1)
        bins_needed = round(population / 200, 1)
        efficiency = round(random.uniform(75, 95), 1)
        ai_advice = random.choice([
            "Increase composting initiatives.",
            "Optimize bin collection schedule.",
            "Promote recycling awareness.",
            "Monitor high-waste zones using IoT sensors.",
            "Introduce waste segregation points."
        ])

        result = {
            "city": city.title(),
            "population": int(population),
            "avg_waste": avg_waste,
            "predicted_tomorrow": predicted_tomorrow,
            "weekly_total": weekly_total,
            "monthly_total": monthly_total,
            "recyclable": recyclable,
            "landfill": landfill,
            "carbon_emission": carbon_emission,
            "trucks_needed": trucks_needed,
            "bins_needed": bins_needed,
            "efficiency": efficiency,
            "ai_advice": ai_advice
        }

    return render_template("index.html", result=result)


# ✅ Use waitress for production (No warnings)
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
