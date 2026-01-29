from flask import Flask, request, render_template

# Flask-applicatie initialiseren
app = Flask(__name__)

# Route voor de hoofdpagina
@app.route("/")
def main():
    # HTML-template weergeven
    return render_template("index.html")

# Applicatie starten
# host="0.0.0.0" is nodig zodat de app bereikbaar is vanuit de Docker container
# port=8080 komt overeen met de exposed Docker-poort
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
