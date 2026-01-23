import json
import requests
requests.packages.urllib3.disable_warnings()

ROUTER = "192.168.56.102"

url = f"https://{ROUTER}/restconf/data/ietf-interfaces:interfaces/interface=Loopback4"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

auth = ("cisco", "cisco123!")

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback4",
        "description": "N4 RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.4.4.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

print("Loopback configureren via RESTCONF...")

response = requests.put(
    url,
    auth=auth,
    headers=headers,
    data=json.dumps(payload),
    verify=False
)

if 200 <= response.status_code <= 299:
    print("OK - configuratie toegepast:", response.status_code)
else:
    print("FOUT:", response.status_code)
    print(response.text)

