import json

# Gesimuleerde Webex API response (JSON)
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

# JSON omzetten naar Python dictionary
data = json.loads(webex_data)

# Filter: enkel personen tonen met naam en e-mail
for user in data["items"]:
    if user.get("type") == "person":
        name = user.get("displayName")
        email = user.get("emails")[0]
        print("Naam:", name, "| Email:", email)
