from ncclient import manager
import xml.dom.minidom

with manager.connect(
    host="192.168.56.102",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:

    print("NETCONF sessie gestart")

    netconf_filter = """
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
    </filter>
    """

    reply = m.get_config(
        source="running",
        filter=netconf_filter
    )

    print(xml.dom.minidom.parseString(
        reply.xml).toprettyxml())
