# Importeer de ConnectHandler class uit de Netmiko library
# Deze class wordt gebruikt om via SSH verbinding te maken met een router
from netmiko import ConnectHandler

# Routergegevens voor de SSH-verbinding
router = {
    "device_type": "cisco_ios",      # Type toestel (Cisco IOS)
    "host": "192.168.56.102",         # IP-adres van de router
    "username": "cisco",              # SSH gebruikersnaam
    "password": "cisco123!",          # SSH wachtwoord
}

# Informatieve melding
print("🔗 Verbinden met router via NETMIKO (SSH)...")

# Maak de SSH-verbinding met de router
net_connect = ConnectHandler(**router)

# Lijst van configuratiecommando’s
# Deze commando’s worden in configuratiemodus uitgevoerd
config_commands = [
    "interface Loopback2222",
    "ip address 10.10.22.22 255.255.255.255",
    "description Configured via Netmiko"
]

# Stuur de configuratiecommando’s naar de router
output = net_connect.send_config_set(config_commands)

# Toon de output van de configuratie
print(output)

# Verbreek de SSH-verbinding netjes
net_connect.disconnect()

# Bevestiging dat de sessie is afgesloten
print("✅ NETMIKO SSH sessie gesloten")
