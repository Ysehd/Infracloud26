import requests
import urllib.parse

API_KEY = "6ddb2e48-7990-4d65-a40a-bfd414f25382"
GEOCODE_URL = "https://graphhopper.com/api/1/geocode?"
ROUTE_URL = "https://graphhopper.com/api/1/route?"

def geocode(city):
    if city == "":
        return None

    url = GEOCODE_URL + urllib.parse.urlencode({
        "q": city,
        "limit": 1,
        "key": API_KEY
    })

    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    if len(data["hits"]) == 0:
        return None

    lat = data["hits"][0]["point"]["lat"]
    lng = data["hits"][0]["point"]["lng"]
    name = data["hits"][0]["name"]
    country = data["hits"][0].get("country", "")

    location_name = f"{name}, {country}" if country else name
    return lat, lng, location_name


while True:
    start = input("Starting location (q to quit): ")
    if start.lower() in ["q", "quit"]:
        break

    end = input("Destination (q to quit): ")
    if end.lower() in ["q", "quit"]:
        break

    vehicle = input("Vehicle (car / bike / foot): ").lower()
    if vehicle not in ["car", "bike", "foot"]:
        vehicle = "car"

    origin = geocode(start)
    destination = geocode(end)

    if not origin or not destination:
        print("Location not found. Try again.")
        print("-------------------------------------------------")
        continue

    route_url = ROUTE_URL + urllib.parse.urlencode({
        "key": API_KEY,
        "vehicle": vehicle
    })

    route_url += f"&point={origin[0]},{origin[1]}"
    route_url += f"&point={destination[0]},{destination[1]}"

    route_response = requests.get(route_url)
    if route_response.status_code != 200:
        print("Routing error")
        continue

    route_data = route_response.json()
    path = route_data["paths"][0]

    distance_km = path["distance"] / 1000
    time_sec = path["time"] / 1000

    h = int(time_sec // 3600)
    m = int((time_sec % 3600) // 60)
    s = int(time_sec % 60)

    print("=================================================")
    print(f"Route from {origin[2]} to {destination[2]} by {vehicle}")
    print(f"Distance: {distance_km:.2f} km")
    print(f"Duration: {h:02d}:{m:02d}:{s:02d}")
    print("-------------------------------------------------")

    for step in path["instructions"]:
        step_km = step["distance"] / 1000
        print(f"- {step['text']} ({step_km:.2f} km)")

    print("=================================================")
