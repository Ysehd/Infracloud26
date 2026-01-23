from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ DI2 OK – Flask draait in Docker"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
