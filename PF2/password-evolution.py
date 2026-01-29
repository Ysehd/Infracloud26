# Import voor One-Time Passwords (nog niet gebruikt hier)
import pyotp

# SQLite database module
import sqlite3

# Hashing library voor wachtwoorden
import hashlib

# Voor unieke identifiers (nog niet gebruikt hier)
import uuid

# Flask web framework
from flask import Flask, request

# Maak Flask applicatie
app = Flask(__name__)

# Naam van de database
db_name = 'test.db'


# Root endpoint
# Test of de applicatie werkt
@app.route('/')
def index():
    return 'Welcome to the hands-on lab for an evolution of password systems!'


#########################################
# VERSION 1: Plain Text Passwords
# Onveilig. Alleen voor demo.
#########################################

# Signup endpoint versie 1
# Slaat wachtwoorden in plain text op
@app.route('/signup/v1', methods=['POST'])
def signup_v1():

    # Maak verbinding met SQLite database
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Maak tabel aan indien niet bestaat
    # Password wordt onversleuteld opgeslagen
    c.execute(
        '''CREATE TABLE IF NOT EXISTS USER_PLAIN
           (USERNAME TEXT PRIMARY KEY NOT NULL,
            PASSWORD TEXT NOT NULL);'''
    )
    conn.commit()

    try:
        # Voeg gebruiker toe aan database
        # SQL injectie risico (bewust onveilig)
        c.execute(
            "INSERT INTO USER_PLAIN (USERNAME,PASSWORD) "
            "VALUES ('{0}', '{1}')".format(
                request.form['username'],
                request.form['password']
            )
        )
        conn.commit()

    # Fout als username al bestaat
    except sqlite3.IntegrityError:
        return "username has been registered."

    # Print gegevens naar console (onveilig)
    print('username: ', request.form['username'],
          ' password: ', request.form['password'])

    return "signup success"


# Controleer plain text wachtwoord
def verify_plain(username, password):

    # Verbind met database
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    # Haal wachtwoord op
    query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}'".format(
        username)
    c.execute(query)

    # Haal resultaat op
    records = c.fetchone()
    conn.close()

    # Geen gebruiker gevonden
    if not records:
        return False

    # Vergelijk plain text wachtwoord
    return records[0] == password


# Login endpoint versie 1
@app.route('/login/v1', methods=['GET', 'POST'])
def login_v1():
    error = None

    # Alleen POST toegestaan
    if request.method == 'POST':

        # Controleer login
        if verify_plain(request.form['username'], request.form['password']):
            error = 'login success'
        else:
            error = 'Invalid username/password'

    else:
        error = 'Invalid Method'

    return error


#########################################
# VERSION 2: Password Hashing
# Veiliger dan plain text
#########################################

# Signup endpoint versie 2
# Gebruikt hashing
@app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():

    # Verbind met database
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Tabel voor gehashte wachtwoorden
    c.execute(
        '''CREATE TABLE IF NOT EXISTS USER_HASH
           (USERNAME TEXT PRIMARY KEY NOT NULL,
            HASH TEXT NOT NULL);'''
    )
    conn.commit()

    try:
        # Hash het wachtwoord met SHA-256
        hash_value = hashlib.sha256(
            request.form['password'].encode()).hexdigest()

        # Sla username en hash op
        c.execute(
            "INSERT INTO USER_HASH (USERNAME, HASH) "
            "VALUES ('{0}', '{1}')".format(
                request.form['username'],
                hash_value
            )
        )
        conn.commit()

    # Username bestaat al
    except sqlite3.IntegrityError:
        return "username has been registered."

    # Print debug info
    print('username: ', request.form['username'],
          ' password: ', request.form['password'],
          ' hash: ', hash_value)

    return "signup success"


# Controleer gehashed wachtwoord
def verify_hash(username, password):

    # Verbind met database
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Haal hash op
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(
        username)
    c.execute(query)

    records = c.fetchone()
    conn.close()

    # Geen gebruiker
    if not records:
        return False

    # Hash invoer en vergelijk
    return records[0] == hashlib.sha256(password.encode()).hexdigest()


# Login endpoint versie 2
@app.route('/login/v2', methods=['GET', 'POST'])
def login_v2():
    error = None

    # Alleen POST
    if request.method == 'POST':

        # Controleer login
        if verify_hash(request.form['username'], request.form['password']):
            error = 'login success'
        else:
            error = 'Invalid username/password'

    else:
        error = 'Invalid Method'

    return error


#########################################
# Start Flask applicatie
#########################################

if __name__ == '__main__':

    # Start server op alle interfaces
    # HTTPS met self-signed cert
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
