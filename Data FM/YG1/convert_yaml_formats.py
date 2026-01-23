import yaml
import json
import csv

# Gesimuleerde YAML-data (netwerkconfiguratie)
yaml_input = """
devices:
  - hostname: Switch1
    ip: 10.0.0.2
    location: ServerRoom
  - hostname: Switch2
    ip: 10.0.0.3
    location: Office
"""

# YAML → Python dictionary
data = yaml.safe_load(yaml_input)
print("Python dict:")
print(data)

# Python dict → JSON
json_output = json.dumps(data, indent=2)
print("\nJSON output:")
print(json_output)

# Python dict → CSV
with open("devices.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hostname", "IP", "Location"])

    for device in data["devices"]:
        writer.writerow([
            device["hostname"],
            device["ip"],
            device["location"]
        ])

print("\nCSV-bestand aangemaakt: devices.csv")
