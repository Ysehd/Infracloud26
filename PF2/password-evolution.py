from flask import Flask, request
import sqlite3
import hashlib
import os

app = Flask(__name__)
DB_NAME = "test.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS USER_PLAIN (
        USERNAME TEXT PRIMARY KEY,
        PASSWORD TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS USER_HASH (
        USERNAME TEXT PRIMARY KEY,
        HASH TEXT
    )""")

    conn.commit()
    conn.close()

@app.route('/signup/v1', methods=['POST'])
def signup_plain():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO USER_PLAIN VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

    return "Plain signup OK"

@app.route('/login/v1', methods=['POST'])
def login_plain():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM USER_PLAIN WHERE USERNAME=? AND PASSWORD=?", (username, password))
    result = c.fetchone()
    conn.close()

    return "Plain login OK" if result else "Plain login FAILED"

@app.route('/signup/v2', methods=['POST'])
def signup_hash():
    username = request.form['username']
    password = request.form['password']
    hash_value = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO USER_HASH VALUES (?,?)", (username, hash_value))
    conn.commit()
    conn.close()

    return "Hash signup OK"

@app.route('/login/v2', methods=['POST'])
def login_hash():
    username = request.form['username']
    password = request.form['password']
    hash_value = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM USER_HASH WHERE USERNAME=? AND HASH=?", (username, hash_value))
    result = c.fetchone()
    conn.close()

    return "Hash login OK" if result else "Hash login FAILED"

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)
