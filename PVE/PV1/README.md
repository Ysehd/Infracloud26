In dit experiment werd een Python virtual environment gebruikt om een project
geïsoleerd uit te voeren. De virtual environment werd aangemaakt met venv en
geactiveerd zodat Python en pip vanuit deze omgeving gebruikt werden. Binnen
deze omgeving werd het Python package requests geïnstalleerd en gebruikt in
een eigen Python script dat een REST API-aanroep uitvoert naar httpbin.org.
Alle bestanden van de virtual environment werden automatisch door Python
gegenereerd en niet aangepast. Dit experiment toont het belang van dependency
isolatie en het gebruik van virtual environments als best practice binnen
DevOps en automation.


pip list pour voir si tout a etait installer
Pv1 – Python Virtual Environment (venv)

Belangrijke commando’s
venv maken: python3 -m venv venv
venv activeren: source venv/bin/activate
packages installeren: pip install flask
app starten: python3 app.py
Controleren: sudo lsof -i :5050
venv stoppen: deactivate