import json

# Gesimuleerde JSON-output van een netwerkdevice
device_response = """
{
  "interfaces": [
    {
      "interface_name": "GigabitEthernet1/0",
      "ipv4": "192.168.100.1",
      "admin_state": "up"
    },
    {
      "interface_name": "GigabitEthernet1/1",
      "ipv4": "unassigned",
      "admin_state": "down"
    },
    {
      "interface_name": "Loopback10",
      "ipv4": "10.10.10.10",
      "admin_state": "up"
    }
  ]
}
"""

# JSON omzetten naar Python dictionary
network_info = json.loads(device_response)

# Filter: toon alleen actieve interfaces met een IP-adres
for iface in network_info["interfaces"]:
    if iface.get("admin_state") == "up" and iface.get("ipv4") != "unassigned":
        print("Interface:", iface["interface_name"], "| IP:", iface["ipv4"])
