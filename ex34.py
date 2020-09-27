"""
20200927
Kristin
Uppgift 34

34.1 Lägg till 3 egna nya djur i djur.py från uppgift 33.

Använd wikipedia för att hitta URL:er och för att reda ut eventuella oklarheter kring namn och köttätare/vegetarian. :)

34.2 Lägg till följande metod i Djur klassen:

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vetegarian"

Byt ut if-else blocken i programmet mot anrop till denna metod!

34.3 Bygg en metod "get_html_table_row(self)" i klassen Djur, och flytta in f-stringen med <tr><td> etc in i Djurklassen.
Anropa denna istället för att bygga upp HTML-koden i forloopen. Obs! Låt <html><table> d.v.s det som ligger "runtom"
tabelldatan vara kvar i huvudprogrammet - flytta inte in detta i Djurklassen.
Tips: för att anropa en metod ifrån en annan metod, använd syntaxen self.metod2(arg1, arg2). Kan vara användbart
för att bygga get_html_table_row ;)
"""

import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("ex34_djur.html")
TEMPLATE_PATH = Path('ex34_djur_template.html')

class Djur:
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vegetarian"

    def get_html_table_row(self):
        table_row = f'<tr><td><a href="{self.wiki_url}">{self.name}</td><td>{self.carnivore_or_vegetarian()}</td></tr>\n'
        return table_row


if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    myrkotte = Djur('Myrkotte', True, 'https://sv.wikipedia.org/wiki/Myrkottar')
    sköldpadda = Djur('Sköldpadda', False, 'https://sv.wikipedia.org/wiki/Sk%C3%B6ldpaddor')
    älg = Djur('Älg', False, 'https://sv.wikipedia.org/wiki/%C3%84lgar')
    djur.append(zebra)
    djur.append(tiger)
    djur.append(myrkotte)
    djur.append(sköldpadda)
    djur.append(älg)

    table_rows = ""
    for d in djur:
        table_rows += d.get_html_table_row()
    html = TEMPLATE_PATH.read_text()
    html = html.replace('TABLE_ROWS', table_rows)
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))
