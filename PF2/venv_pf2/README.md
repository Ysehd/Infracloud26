Bij de hashed signup endpoint krijg ik een HTTP 500 omdat de gebruiker al bestaat en er geen exception handling is voorzien.
De gebruiker wordt wel correct opgeslagen en de hashed login werkt, wat bewijst dat hashing en database-interactie correct functioneren.
De 500-fout bij signup gebeurt wanneer een username al bestaat.
Dit komt door de PRIMARY KEY-constraint in SQLite en toont aan dat de database correct werkt.
Login blijft correct functioneren, wat bevestigt dat de applicatie werkt zoals verwacht.

terminal
cd ~/Infracloud26/PF2

prompt wordt venv_2
source venv_pf2/bin/activate

python3 password-evolution.py

tweede terminal
cd ~/Infracloud26/PF2
source venv_pf2/bin/activate

curl -X POST -F "username=alia" -F "password=1234" http://localhost:5000/signup/v1

curl -X POST -F "username=alia" -F "password=1234" http://localhost:5000/login/v1


curl -X POST -F "username=bob" -F "password=5678" http://localhost:5000/signup/v2

curl -X POST -F "username=bob" -F "password=5678" http://localhost:5000/login/v2




PF2 – Login Page Experiment

In dit experiment werd een Flask-applicatie gebouwd om gebruikersauthenticatie te testen met zowel plain text als gehashte wachtwoorden. De applicatie draait in een Python virtual environment en gebruikt een SQLite-database voor opslag. Via de endpoints /signup/v1 en /login/v1 worden wachtwoorden in plain text opgeslagen en gecontroleerd, wat functioneel maar onveilig is. Via /signup/v2 en /login/v2 worden wachtwoorden eerst gehasht met SHA256 voordat ze in de database worden opgeslagen, wat een veiligere aanpak is. De werking werd getest met curl-commando’s en de resultaten werden geverifieerd in de database. Dit experiment toont het verschil aan tussen onveilige en veilige wachtwoordopslag en benadrukt het belang van hashing bij gebruikersauthenticatie.


Flask is een lichtgewicht Python framework dat wordt gebruikt om een webserver en API te bouwen. In dit project gebruik ik Flask om een API te maken die via HTTP-requests gebruikers kan laten registreren en inloggen. De applicatie luistert op poort 5000 en verwerkt POST-requests via verschillende routes.

In versie 1 worden wachtwoorden in plain text opgeslagen in een SQLite-database, wat onveilig is. In versie 2 worden wachtwoorden eerst gehasht met SHA256, waardoor het echte wachtwoord niet wordt opgeslagen. De werking van de API wordt getest met curl in plaats van een browser. De Flask-waarschuwing over de development server is normaal en geen fout.




Flask is een lichtgewicht Python webframework dat wordt gebruikt om eenvoudige webservers en API’s te bouwen. In dit project gebruik ik Flask niet om een klassieke website te maken, maar om een API te bouwen. Een API is een manier waarop programma’s met elkaar communiceren via HTTP-verzoeken, zonder grafische interface. De Flask-app luistert op poort 5000 en verwerkt POST-requests voor signup en login via verschillende routes.

Elke route in Flask bepaalt wat er moet gebeuren wanneer een bepaald endpoint wordt aangesproken. In mijn applicatie zijn er twee versies van login en signup. In versie 1 worden gebruikersnamen en wachtwoorden in plain text opgeslagen in een SQLite-database. Dit is onveilig, maar wordt gebruikt om het probleem duidelijk te maken. In versie 2 worden wachtwoorden eerst gehasht met het SHA256-algoritme voordat ze worden opgeslagen. Hierdoor wordt het echte wachtwoord nooit in de database bewaard, wat veel veiliger is.

De werking van de API wordt getest met het command-line tool curl, omdat dit project geen webinterface heeft. Een succesvolle response zoals “login OK” toont aan dat de API correct werkt. De SQLite-database wordt lokaal aangemaakt in één bestand en is geschikt voor test- en labo-omgevingen. De waarschuwing die Flask toont over de development server is normaal en geen fout; deze server is bedoeld voor testen en niet voor productiegebruik.

Als je wil, kan ik deze tekst ook:

nog korter maken

vereenvoudigen voor absolute beginners

aanpassen naar examenantwoord-stijl

korter

Flask is een lichtgewicht Python framework dat wordt gebruikt om een webserver en API te bouwen. In dit project gebruik ik Flask om een API te maken die via HTTP-requests gebruikers kan laten registreren en inloggen. De applicatie luistert op poort 5000 en verwerkt POST-requests via verschillende routes.

In versie 1 worden wachtwoorden in plain text opgeslagen in een SQLite-database, wat onveilig is. In versie 2 worden wachtwoorden eerst gehasht met SHA256, waardoor het echte wachtwoord niet wordt opgeslagen. De werking van de API wordt getest met curl in plaats van een browser. De Flask-waarschuwing over de development server is normaal en geen fout.

geeef antwoorden op alle soortenv ragen 

Hier is een overzicht met antwoorden op alle soorten vragen die je kan krijgen over PF2 / Flask / API, kort, duidelijk en examenproof.
Je kan dit gebruiken om te studeren of mondeling te antwoorden.

Algemene vragen

Wat is Flask?
Flask is een lichtgewicht Python webframework waarmee je snel een webserver of API kan bouwen.

Waarom gebruik je Flask?
Omdat het eenvoudig is, weinig code nodig heeft en ideaal is voor kleine projecten en labo’s.

Is Flask een website?
Nee, in dit project is Flask een API, geen website met een interface.

API-vragen

Wat is een API?
Een API is een manier waarop programma’s met elkaar communiceren via HTTP-verzoeken.

Waarom gebruik je een API en geen website?
Omdat een API bedoeld is voor communicatie tussen systemen, niet voor eindgebruikers.

Waarom gebruik je POST en geen GET?
Omdat POST wordt gebruikt om gegevens te versturen (zoals username en password).

Routes & werking

Wat is een route in Flask?
Een route bepaalt wat Flask moet doen wanneer een bepaalde URL wordt aangesproken.

Wat doet /signup?
Het registreert een nieuwe gebruiker in de database.

Wat doet /login?
Het controleert of de gebruikersgegevens correct zijn.

Beveiliging

Wat is plain text opslag?
Wachtwoorden worden onversleuteld in de database opgeslagen.

Waarom is plain text onveilig?
Omdat iedereen met toegang tot de database de wachtwoorden kan lezen.

Wat is hashing?
Hashing zet een wachtwoord om in een vaste, onleesbare waarde.

Waarom is hashing veiliger?
Omdat het echte wachtwoord nooit wordt opgeslagen.

Waarom gebruik je SHA256?
Omdat het een bekende en eenvoudige hashfunctie is voor demonstratie.

Database

Wat is SQLite?
Een lichte database die in één bestand wordt opgeslagen.

Waarom SQLite gebruiken?
Omdat het eenvoudig is en geen aparte server nodig heeft.

Waarom krijg je soms een 500 error bij signup?
Omdat je een bestaande gebruiker opnieuw probeert toe te voegen (PRIMARY KEY).

Testen

Waarom test je met curl?
Omdat dit een API is en geen website.

Hoe weet je dat de API werkt?
Als curl “login OK” of “signup OK” teruggeeft.

Waarom zie je niets in de browser?
Omdat er geen homepage (/) is gedefinieerd.

Flask-meldingen

Wat betekent “This is a development server”?
Dat Flask bedoeld is voor testen, niet voor productie.

Is dat een fout?
Nee, dit is normaal.

Wat betekent “port already in use”?
Dat de Flask-server al draait op die poort.

Vergelijkingsvragen

Verschil tussen v1 en v2?

v1: plain text, onveilig

v2: hashing, veiliger

Wat heb je geleerd met PF2?
Het verschil tussen onveilige en veilige wachtwoordopslag en hoe een API werkt.

Perfecte afsluitzin (onthouden)

“In PF2 heb ik met Flask een API gebouwd die gebruikers kan registreren en laten inloggen, waarbij ik het verschil toon tussen plain text wachtwoorden en gehashte wachtwoorden met SHA256.”

Virtual Environment (venv)

Wat is een virtual environment (venv)?
Een virtual environment is een afgesloten Python-omgeving waarin je libraries installeert die alleen voor dat project gelden.

Waarom gebruik je een venv?
Om conflicten te vermijden tussen Python-packages van verschillende projecten.

Wat gebeurt er zonder venv?
Alle libraries worden globaal geïnstalleerd en kunnen andere projecten breken.