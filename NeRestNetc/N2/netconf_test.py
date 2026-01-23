








from ncclient import manager

hostname_config = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <hostname>NETCONF-ROUTER</hostname>
 </native>
</config>
"""

with manager.connect(
    host="192.168.56.102",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:

    m.edit_config(target="running", config=hostname_config)
    print("✅ Hostname aangepast via NETCONF")
from ncclient import manager

print("🔗 Verbinden met router via NETCONF...")

with manager.connect(
    host="192.168.56.102",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:

    print("✅ NETCONF sessie gestart\n")

    print("📄 Ondersteunde NETCONF capabilities:")
    for cap in m.server_capabilities:
        print(cap)

    print("\n🏷️ Hostname aanpassen via NETCONF...")

    hostname_config = """
    <config>
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <hostname>NETCONF-OK</hostname>
     </native>
    </config>
    """

    m.edit_config(target="running", config=hostname_config)
    print("✅ Hostname aangepast via NETCONF")

