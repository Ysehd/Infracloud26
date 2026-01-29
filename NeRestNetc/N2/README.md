terminal
cd ~/Infracloud26/NeRestNetc/N3
ls

python3 netmico_test.py

router
enable
show running-config | include hostname

optioneel sessie bevestigen
show netmico-yang sessions

router logs controleren
show logging | include NETMICO



Netmiko is een Python-library die netwerkautomatisatie mogelijk maakt via SSH. In deze opdracht heb ik Netmiko gebruikt om automatisch verbinding te maken met een Cisco-router. 

Vanuit een Python-script heb ik een SSH-sessie opgezet met de router door het IP-adres, gebruikersnaam en wachtwoord te configureren. 
Na het opzetten van de verbinding heb ik via Netmiko het commando show ip interface brief uitgevoerd, waarna de router de interface-informatie teruggaf aan het script. 

Dit toont aan dat de communicatie volledig via SSH verloopt en dat Netmiko succesvol commando’s kan uitvoeren op het netwerktoestel. 

De actieve SSH-verbinding is zichtbaar op de router met de commando’s show users en show ssh. Na het uitvoeren van het commando werd de SSH-sessie correct afgesloten.

Via Netmiko werd een configuratie naar de router gestuurd die een loopback-interface aanmaakt en een IP-adres toekent. De configuratie is zichtbaar in de running-config, wat aantoont dat de wijziging succesvol werd toegepast via SSH.




Deze Python-code gebruikt NETCONF via de ncclient library om op een Cisco IOS XE router de hostname aan te passen. Eerst wordt een XML-configuratie opgesteld volgens het Cisco IOS XE YANG-model, waarin de nieuwe hostname wordt gedefinieerd.

 Vervolgens maakt het script via SSH poort 830 een NETCONF-verbinding met de router. Met de functie edit_config() wordt deze XML-configuratie transactioneel naar de running datastore gestuurd, wat betekent dat de wijziging alleen wordt toegepast als ze volledig geldig is. 
 
 Daarna toont het script de ondersteunde NETCONF-capabilities van de router en bevestigt het dat de hostname succesvol is aangepast. 
 
 Dit bewijst dat de configuratie model-driven, gestructureerd en zonder CLI-commando’s is uitgevoerd.