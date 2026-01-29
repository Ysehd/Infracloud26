Terminal
cd ~/Infracloud26/NeRestNetc/N4
ls


python3 netconf_get.py

python3 netconf_test.py

ROUTER
enable
show ip interface brief
show running-config | section Loopback4


In N4 moest ik NETCONF gebruiken om een Cisco IOS XE-router te beheren via YANG-modellen. Vanuit de DEVASC-VM heb ik via NETCONF verbinding gemaakt met de router over SSH poort 830. Met een NETCONF GET-config heb ik configuratie- en interfacegegevens opgehaald en met edit-config heb ik een loopback-interface geconfigureerd volgens het Cisco IOS XE native YANG-datamodel. De configuratie werd correct toegepast zonder fouten, wat bevestigd werd door geldige NETCONF-responses en door verificatie op de router. Eventuele meldingen in de output waren niet-kritische application-level warnings en hadden geen invloed op de werking. Hiermee heb ik aangetoond dat ik NETCONF kan gebruiken om netwerkconfiguratie gestructureerd, transactioneel en betrouwbaar te beheren.

In N4 heb ik NETCONF gebruikt om via YANG-modellen configuratie op een Cisco IOS XE-router te lezen en te wijzigen.

SSH poort 830 is de standaardpoort voor NETCONF.
NETCONF gebruikt SSH als transport, maar niet de gewone SSH-poort 22. In plaats daarvan luistert een netwerkapparaat (zoals een Cisco IOS XE-router) op poort 830 om NETCONF-sessies te accepteren. Zo kan het toestel NETCONF-verkeer onderscheiden van normale CLI-SSH-sessies.

NETCONF en RESTCONF zijn beide netwerkbeheerprotocollen die met YANG-modellen werken, maar ze verschillen in aanpak. NETCONF gebruikt SSH op poort 830, werkt met XML en is transactioneel, wat betekent dat configuraties volledig worden toegepast of helemaal niet. RESTCONF gebruikt HTTPS, werkt met JSON of XML en volgt REST-principes zoals GET en PUT, waardoor het eenvoudiger en meer API-gericht is, maar minder strikt dan NETCONF.

Daarna heb ik op de DEVASC-VM RESTCONF-requests uitgevoerd. Eerst heb ik met een GET-request de interfacegegevens van de router opgehaald. Dit deed ik via Postman en daarna via een Python-script met de requests-library. De router antwoordde met HTTP statuscode 200 en gaf de interface-informatie terug in YANG-JSON-formaat. Vervolgens heb ik met een PUT-request een loopback-interface geconfigureerd. In deze configuratie heb ik de interface-naam, een beschrijving en een IPv4-adres opgegeven volgens het ietf-interfaces YANG-model. Deze PUT-request werd eveneens via Postman en via Python uitgevoerd en de router bevestigde dit met HTTP statuscode 201.

Tot slot heb ik op de router gecontroleerd of de configuratie correct was toegepast door de interfaces en de running-config te bekijken. De nieuwe loopback-interface was zichtbaar en actief, en in de routerlogs stond dat de configuratie via NETCONF/RESTCONF was uitgevoerd. Hiermee heb ik aangetoond dat ik RESTCONF kan gebruiken om configuratie en statusinformatie op een Cisco IOS XE-apparaat te lezen en te wijzigen op een gestructureerde en transactionele manier.


Wat betekent dit écht?

IOS XE probeert IPv6-informatie te tonen

Maar GigabitEthernet1 heeft geen geldige IPv6-config

Cisco IOS XE is hier slordig en stuurt een partial error mee

Dit is GEEN fatale fout
Dit breekt je request niet
Dit stopt RESTCONF niet