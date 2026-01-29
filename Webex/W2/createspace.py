import requests

# Webex access token voor authenticatie
ACCESS_TOKEN = "JE_ACCESS_TOKEN_HIER"

# HTTP headers met Bearer token en JSON content type
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# ------------------------
# SPACE AANMAKEN
# ------------------------

# URL voor het aanmaken van een Webex space
create_url = "https://webexapis.com/v1/rooms"

# Payload met de naam van de space
create_payload = {
    "title": "DevNet Automation Space"
}

# Verstuur een POST-request om de space aan te maken
create_response = requests.post(
    create_url,
    headers=headers,
    json=create_payload
)

# Controleer of de space succesvol is aangemaakt
if create_response.status_code in [200, 201]:
    # Haal het ID van de aangemaakte space op
    room_id = create_response.json()["id"]
    print("Space aangemaakt met ID:", room_id)
else:
    # Foutmelding bij mislukte creatie
    print("Fout bij aanmaken space")
    exit()

# ------------------------
# SPACE VERWIJDEREN
# ------------------------

# URL voor het verwijderen van de aangemaakte space
delete_url = f"https://webexapis.com/v1/rooms/{room_id}"

# Verstuur een DELETE-request om de space te verwijderen
delete_response = requests.delete(
    delete_url,
    headers=headers
)

# Controleer of de space succesvol werd verwijderd
if delete_response.status_code == 204:
    print("Space succesvol verwijderd")
else:
    # Foutmelding bij mislukte verwijdering
    print("Fout bij verwijderen space")
