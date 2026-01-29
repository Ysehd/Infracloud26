In deze opdracht wordt een Flask webapplicatie gebruikt om wachtwoordbeveiliging te testen.
De applicatie toont twee versies van authenticatie.

In versie 1 worden wachtwoorden in plain text opgeslagen, wat onveilig is.
In versie 2 worden wachtwoorden gehashed met SHA-256, wat veiliger is.

Met curl worden HTTP requests gestuurd om gebruikers te registreren en in te loggen.
Zo wordt duidelijk hoe hashing werkt en waarom plain text passwords een risico zijn.


PF2 

nohup python3 password-evolution.py &

curl -k https://0.0.0.0:5000/

niet gehashd
curl -k -X POST -F "username=alice" -F "password=myalicepassword" https://0.0.0.0:5000/signup/v1
curl -k -X POST -F "username=bob" -F "password=passwordforbob" https://0.0.0.0:5000/signup/v1

dit is gehashd
curl -k -X POST -F "username=rick"  -F "password=samepassword" https://0.0.0.0:5000/signup/v2
curl -k -X POST -F "username=allan" -F "password=samepassword" https://0.0.0.0:5000/signup/v2
curl -k -X POST -F "username=dave"  -F "password=differentpassword" https://0.0.0.0:5000/signup/v2

testen 
curl -k -X POST -F "username=rick"  -F "password=samepassword" https://0.0.0.0:5000/login/v2
curl -k -X POST -F "username=allan" -F "password=wrongpassword" https://0.0.0.0:5000/login/v2
curl -k -X POST -F "username=allan" -F "password=samepassword" https://0.0.0.0:5000/login/v2
curl -k -X POST -F "username=dave"  -F "password=differentpassword" https://0.0.0.0:5000/login/v2

niet gehashd v1
# curl            → command-line tool om HTTP/HTTPS requests te sturen
# -k              → accepteert een self-signed SSL-certificaat (Flask adhoc TLS)
# -X POST         → gebruikt de HTTP POST-methode om data te verzenden
# -F              → stuurt form data (zoals een HTML formulier)
# username=alice  → username veld dat Flask leest via request.form['username']
# password=...    → plaintext wachtwoord (wordt ONGEHASHED opgeslagen)
# /signup/v1      → endpoint dat plaintext passwords opslaat in USER_PLAIN tabel

curl -k -X POST -F "username=alice" -F "password=myalicepassword" https://0.0.0.0:5000/signup/v1




Hashed password signup (v2)
# curl              → command-line HTTP client
# -k                → negeert fout van self-signed SSL-certificaat
# -X POST           → POST request om data te versturen
# -F                → form fields (username + password)
# username=rick     → username dat wordt opgeslagen
# password=...      → wachtwoord dat eerst wordt gehasht met SHA-256
# /signup/v2        → endpoint dat HASHES opslaat in USER_HASH tabel

curl -k -X POST -F "username=rick" -F "password=samepassword" https://0.0.0.0:5000/signup/v2
