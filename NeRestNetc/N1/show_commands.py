from netmiko import ConnectHandler
# Importeert ConnectHandler uit Netmiko
# Netmiko wordt gebruikt om netwerkapparaten te beheren via SSH

# Dictionary met routergegevens
# Deze info is nodig om verbinding te maken
router = {
    "device_type": "cisco_ios",   # Type netwerkdevice (Cisco IOS)
    "host": "192.168.56.103",     # IP-adres van de router
    "username": "cisco",          # SSH gebruikersnaam
    "password": "cisco123!",      # SSH wachtwoord
}

print("🔗 Verbinden met router...")
# Geeft aan dat de SSH-verbinding start

# Maakt een SSH-verbinding met de router
# **router geeft de parameters door
connection = ConnectHandler(**router)

print("📡 Uitvoeren: show ip interface brief")
# Geeft aan welk commando wordt uitgevoerd

# Stuurt een CLI-commando naar de router
# Dit commando toont interface status en IP-adressen
output = connection.send_command("show ip interface brief")

# Print de output van de router in de terminal
print(output)

# Sluit de SSH-verbinding
connection.disconnect()

print("✅ Verbinding gesloten")
# Bevestigt dat de verbinding correct is afgesloten
