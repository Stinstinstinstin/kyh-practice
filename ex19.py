"""
20200924
Kristin
Uppgift 19

Spara följande i "data.json":

[
  12,
  3.5,
  4,
  true,
  false,
  "vi kan ha text också",
  "1234908",
  "99999999",
  {
    "fredrik": {
      "tfn": "12345677",
      "adress": "Banangränd",
      "email": "freddan@proagile.se"
    }
  }
]

Uppgift:
Läs in "data.json" i Python, spara i en variabel "data = json.loads(content)" i Python.
Med hjälp av debuggern, undersök datatyper ni kan hitta inuti data-variabeln.
Posta alla datatyper ni hittar som kommentarer i denna uppgift!
"""

import json
from pprint import pprint

# json.load - tar in ett filobjekt
with open("ex19_data.json", "r") as f:
    data = json.load(f)
    print(data)

# json.loads - tar in en sträng
with open("ex19_data.json", "r") as f:
    content = f.read()
    data = json.loads(content)
    pprint(data)

"""
Hittar följande datatyper; int, float, bool, str, dict
"""
