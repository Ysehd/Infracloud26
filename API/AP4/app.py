from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://jsonplaceholder.typicode.com/users"

@app.route("/", methods=["GET", "POST"])
def home():
    user = None
    error = None

    if request.method == "POST":
        user_id = request.form.get("user_id")

        if not user_id or not user_id.isdigit():
            error = "Voer een geldig numeriek ID in."
        else:
            response = requests.get(f"{API_URL}/{user_id}")
            if response.status_code == 200:
                user = response.json()
            else:
                error = "Gebruiker niet gevonden."

    return render_template("form.html", user=user, error=error)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
