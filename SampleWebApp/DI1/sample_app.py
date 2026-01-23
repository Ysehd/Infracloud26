from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", ip=request.remote_addr)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
