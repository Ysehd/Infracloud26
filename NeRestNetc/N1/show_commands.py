from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException, NetmikoAuthenticationException

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

try:
    print("Verbinden met router via SSH...")
    connection = ConnectHandler(**router)

    print("\n--- show version ---")
    output_version = connection.send_command("show version")
    print(output_version)

    print("\n--- show ip interface brief ---")
    output_ip = connection.send_command("show ip interface brief")
    print(output_ip)

    connection.disconnect()
    print("\nVerbinding gesloten.")

except NetmikoAuthenticationException:
    print("Authenticatie mislukt.")

except NetmikoTimeoutException:
    print("Router niet bereikbaar via SSH.")

