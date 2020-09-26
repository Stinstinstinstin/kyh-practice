"""
20200926
Kristin
Uppgift 24

Nu ska vi använda oss av kunskapen kring JSON och att installera paket från PyPI (cheese shop) på riktigt!
Börja med att utöka "requirements.txt" med paketet "requests":
    pygame
    requests
.. och låt PyCharm installera det nya paketet när frågan dyker upp.
1. Pröva att ladda ned denna URL i browsern:
   https://proagile.se/api/publicEvents

2. Läs på hur man gör en GET med requests-API:et (googla!). Gör ett GET-request mot URL ifrån (1) och
skriv ut r.text med print, typ:
    r = requests.get( ... )  # fixa rätt parametrar! r.text är råa strängen som är resultatet

3. Använd nu istället pprint för att skriva ut r.json(). pprint finns i inbyggda modulen "pprint".

4. Vi vill veta exakt när alla kurser börjar på ProAgile. Bygg ett program som letar upp
alla "startDate" i datan, och skriver ut dem!
"""

import requests
from pprint import pprint


r = requests.get('https://proagile.se/api/publicEvents')
# print(f"Statuskod: {r.status_code}")
data = r.json()
# pprint(r.json())

print("Startdatum:")
for i in range(len(data)):
    print(data[i]['startDate'])
