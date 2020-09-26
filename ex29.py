"""
20200926
Kristin
Uppgift 29
Bygg ett Pythonprogram som genererar en random life quote med random getbild!

Hur? Jo genom att utgå ifrån bifogad fil, och byta ut "QUOTE_TEXT" mot get-citat som ni hittar i följande API:
   https://api.adviceslip.com/advice

Gör bara ett GET-request mot det så får ni random life advice!

HTML-fil att utgå ifrån bifogas som "uppgift29_template".html. Spara den i er kyh-practice.

Programmet ska alltså skapa en ny fil "goat_quote.html" där QUOTE_TEXT ersatts av ett nytt quote,
och starta "goat_quote.html" i webbläsaren.

Tips: ni kommer behöva använda requests, webbrowser, och inbyggda replace() funktionen i string.
Diskutera gärna igenom allt ni behöver göra först!
"""

import requests
import webbrowser
from pathlib import Path

OUTPUT_PATH = Path('ex29_goat_quote.html')
TEMPLATE_PATH = Path('ex29_template.html')

x = requests.get('https://api.adviceslip.com/advice')
data = x.json()
quote = data['slip']['advice']

html = TEMPLATE_PATH.read_text()
html = html.replace("QUOTE_TEXT", quote)

OUTPUT_PATH.write_text(html, encoding='utf8')
webbrowser.open(str(OUTPUT_PATH))
