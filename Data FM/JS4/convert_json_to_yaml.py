import json
import yaml

# Gesimuleerde JSON-data van een netwerkdevice
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

# JSON omzetten naar Python dict
data = json.loads(json_input)

# Dict omzetten naar YAML
yaml_result = yaml.dump(data, sort_keys=False)

print(yaml_result)
