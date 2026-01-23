import json
import requests
requests.packages.urllib3.disable_warnings()

ROUTER = "192.168.56.102"

url = f"https://{ROUTER}/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

auth = ("cisco", "cisco123!")

print("Interfaces ophalen via RESTCONF...")

response = requests.get(
    url,
    auth=auth,
    headers=headers,
    verify=False
)

print("HTTP status:", response.status_code)
print(json.dumps(response.json(), indent=4))

