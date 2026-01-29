# RESTCONF - Loopback configureren via REST API

import json
import requests

# SSL-waarschuwingen uitschakelen (labomgeving)
requests.packages.urllib3.disable_warnings()

# IP-adres van de router
ROUTER = "192.168.56.102"

# NETCONF endpoint voor Loopback4
url = f"https://{ROUTER}/restconf/data/ietf-interfaces:interfaces/interface=Loopback4"

# NETCONF headers (YANG JSON)
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# Basic authentication
auth = ("cisco", "cisco123!")

# YANG JSON payload voor Loopback-interface
payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback4",
        "description": "Loopback via RESTCONF",
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

print("Loopback configureren via NETCONF...")

# PUT request sturen
response = requests.put(
    url,
    auth=auth,
    headers=headers,
    data=json.dumps(payload),
    verify=False
)

# Resultaat controleren
if 200 <= response.status_code <= 299:
    print("OK - configuratie toegepast:", response.status_code)
else:
    print("FOUT:", response.status_code)
    print(response.text)
