import json
# Importeert de json module
# Nodig om JSON data te verwerken in Python

# Gesimuleerde Webex API response (JSON)
# Dit stelt data voor die normaal van een API komt
# De data is hier een string in JSON-formaat
webex_data = """
{
  "items": [
    {
      "id": "10",
      "displayName": "Adam",
      "emails": ["adam@student.be"],
      "type": "person"
    },
    {
      "id": "11",
      "displayName": "Sarah",
      "emails": ["sarah@student.be"],
      "type": "person"
    },
    {
      "id": "12",
      "displayName": "Conference Room",
      "type": "room"
    }
  ]
}
"""

# JSON string omzetten naar een Python dictionary
# json.loads leest de JSON tekst
# Resultaat is een Python object (dict)
data = json.loads(webex_data)

# Loop door alle items in de JSON data
# data["items"] is een lijst van gebruikers en ruimtes
for user in data["items"]:

    # Controleer of het item een persoon is
    # Sommige items zijn geen personen (bv. rooms)
    if user.get("type") == "person":

        # Haal de naam van de gebruiker op
        # displayName bevat de zichtbare naam
        name = user.get("displayName")

        # Haal het eerste e-mailadres op
        # emails is een lijst
        # [0] neemt het eerste e-mailadres
        email = user.get("emails")[0]

        # Toon naam en e-mail in de terminal
        print("Naam:", name, "| Email:", email)
