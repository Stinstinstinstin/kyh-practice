"""
20200925
Kristin
Uppgift 21
En repetitionsuppgift på JSON!

21.1 Vi har tillgång till en fil massadata.json. Ladda ner och undersök hur filen ser ut med PyCharm.

21.2 Bygg ett Pythonprogram som summerar alla värden på "total" i filen, och skriver ut på skärmen.

Tips:
 - läs på om den inbyggda funktionen "sum"
 - repetera hur man läser in en .json fil och läser ut data ifrån den

"""

import json
from pprint import pprint

sum = 0
with open("ex21_massadata.json", 'r') as f:
    data = json.load(f)
    #pprint(data)

for entry in data['entries']:
    sum += entry['total']
print(f"Summa: {sum}")

