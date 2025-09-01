from flask import Flask, render_template, request, jsonify
import mysql.connector
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

app = Flask(__name__)

# Hugging Face API
HF_API_URL = "https://api-inference.huggingface.co/models/your-chosen-model"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="first_aid_ai"
)
cursor = db.cursor()

# Offline emergency guide (basic)
offline_guide = {
    "minor_cut": "Clean the wound with water, apply antiseptic, cover with bandage.",
    "burn": "Run cool water over burn for 10-20 minutes, cover with clean cloth.",
    "fainting": "Lay the person flat, elevate legs, keep airway clear.",
    "chest_pain": "Call emergency services immediately.",
    "fever": "Rest, drink fluids, and monitor temperature. Seek doctor if high fever persists."
}

def get_ai_advice(symptom_text):
    try:
        response = requests.post(HF_API_URL, headers=headers, json={"inputs": symptom_text}, timeout=5)
        result = response.json()
        if isinstance(result, list) and "label" in result[0]:
            return result[0]['label']
        else:
            return offline_fallback(symptom_text)
    except:
        return offline_fallback(symptom_text)

def offline_fallback(symptom_text):
    # Basic keyword mapping
    symptom_text = symptom_text.lower()
    for key, advice in offline_guide.items():
        if key.replace("_", " ") in symptom_text or key in symptom_text:
            return advice
    return "Follow standard first-aid steps and seek medical help."

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symptom_text = request.form["symptoms"]
        ai_advice = get_ai_advice(symptom_text)
        severity = "High" if any(word in symptom_text.lower() for word in ["chest", "breath", "faint"]) else "Low"

        # Save to MySQL
        cursor.execute(
            "INSERT INTO symptoms (symptom_text, ai_advice, severity) VALUES (%s, %s, %s)",
            (symptom_text, ai_advice, severity)
        )
        db.commit()

        return jsonify({"advice": ai_advice, "severity": severity})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
