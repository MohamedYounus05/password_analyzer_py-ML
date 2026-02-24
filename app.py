from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# ----------------------------
# Load Model Safely (Production Safe Path)
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# ----------------------------
# Prediction Function
# ----------------------------
def predict_strength(password):
    password_vector = vectorizer.transform([password])
    prediction = model.predict(password_vector)[0]

    if prediction == 0:
        return "Weak 🔴"
    elif prediction == 1:
        return "Medium 🟡"
    else:
        return "Strong 🟢"

# ----------------------------
# Routes
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        password = request.form["password"]
        result = predict_strength(password)

    return render_template("index.html", result=result)

# ----------------------------
# Production Server Config
# ----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    