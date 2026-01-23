import requests

response = requests.get("https://httpbin.org/get")

print("Statuscode:", response.status_code)
print("JSON data:", response.json())
