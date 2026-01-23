import os
import sqlite3
import hashlib
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = os.environ.get("DB_NAME", "users.db")

def db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            salt TEXT NOT NULL,
            pw_hash TEXT NOT NULL
        );
    """)
    conn.commit()
    return conn

def salted_hash(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok")

@app.route("/signup", methods=["POST"])
def signup():
    username = request.json.get("username", "").strip()
    password = request.json.get("password", "")

    if not username or not password:
        return jsonify(error="username and password required"), 400

    salt = uuid.uuid4().hex
    pw_hash = salted_hash(password, salt)

    conn = db()
    try:
        conn.execute(
            "INSERT INTO users (username, salt, pw_hash) VALUES (?, ?, ?)",
            (username, salt, pw_hash)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify(error="username already exists"), 409
    finally:
        conn.close()

    return jsonify(message="signup success"), 201

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "").strip()
    password = request.json.get("password", "")

    if not username or not password:
        return jsonify(error="username and password required"), 400

    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT salt, pw_hash FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return jsonify(error="invalid username/password"), 401

    salt, pw_hash = row
    if salted_hash(password, salt) == pw_hash:
        return jsonify(message="login success"), 200

    return jsonify(error="invalid username/password"), 401

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)
