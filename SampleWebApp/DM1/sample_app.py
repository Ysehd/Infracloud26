from flask import Flask, render_template, request
import datetime
import os

sample = Flask(__name__)

LOG_PATH = os.environ.get("APP_LOG", "/home/myapp/logs/access.log")

def write_log(line: str):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")

@sample.route("/")
def main():
    ip = request.remote_addr
    write_log(f"{datetime.datetime.utcnow().isoformat()}Z ip={ip} path=/")
    return render_template("index.html")

@sample.route("/_health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)