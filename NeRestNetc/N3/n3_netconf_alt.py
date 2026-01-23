from ncclient import manager
import xml.dom.minidom

ROUTER = {
    "host": "192.168.56.102",   # jouw juiste IP
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False
}

def pretty(xml_data):
    return xml.dom.minidom.parseString(xml_data).toprettyxml()

def main():
    print("🔗 Verbinden met router via NETCONF...")

    with manager.connect(**ROUTER) as m:
        print("✅ NETCONF verbinding actief\n")

        # 1️⃣ Capabilities tonen
        print("📦 Ondersteunde NETCONF / YANG capabilities:")
        for cap in m.server_capabilities:
            print(cap)

        # 2️⃣ Running-config ophalen
        print("\n📄 Running-config (Cisco native YANG):")
        netconf_filter = """
        <filter>
          <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
        </filter>
        """
        reply = m.get_config(source="running", filter=netconf_filter)
        print(pretty(reply.xml))

        # 3️⃣ Hostname aanpassen
        print("✏️ Hostname aanpassen via NETCONF...")
        hostname_payload = """
        <config>
          <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname>N3-NETCONF</hostname>
          </native>
        </config>
        """
        m.edit_config(target="running", config=hostname_payload)
        print("✅ Hostname aangepast via NETCONF")

if __name__ == "__main__":
    main()
