import json
import csv

json_input = """
{
  "devices": [
    {
      "hostname": "Router1",
      "management_ip": "192.168.0.10",
      "state": "active"
    },
    {
      "hostname": "Router2",
      "management_ip": "192.168.0.11",
      "state": "inactive"
    }
  ]
}
"""

data = json.loads(json_input)

with open("devices.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hostname", "Management IP", "State"])

    for device in data["devices"]:
        writer.writerow([
            device["hostname"],
            device["management_ip"],
            device["state"]
        ])

print("CSV-bestand succesvol aangemaakt")
