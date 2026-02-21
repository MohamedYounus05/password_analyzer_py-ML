from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_strength(password):
    password_vector = vectorizer.transform([password])
    prediction = model.predict(password_vector)[0]

    if prediction == 0:
        return "Weak 🔴"
    elif prediction == 1:
        return "Medium 🟡"
    else:
        return "Strong 🟢"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        password = request.form["password"]
        result = predict_strength(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
