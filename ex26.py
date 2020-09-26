"""
20200926
Kristin
Uppgift 26

Nu ska vi leka med att skicka parametrar till ett webb-API!

OMDB är en IMDB-liknande hemsida på nätet, som också tillhandahåller
ett API där man kan göra sökningar.

26.1 Jag har fixat en API-nyckel åt oss! Därför kan vi använda detta
     webb-API (som är ett REST-API) och leka. Testa att skriva följande
     i en browser:

      http://www.omdbapi.com/?t=Alien&apikey=9f6d550c

     Ändra på "Alien" till en annan film!

26.2 Använd requests.get() med ovanstående URL, fast ta bort ? och framåt.
     Använd istället params={"t": "Alien", "apikey": "9f6d550c"} så kommer
     requests att lägga på ? och & och sånt strunt själv. :)

     Pretty printa (pprint) JSON-resultatet från webbanropet med ett Pythonprogram!

26.3 Bygg ett Pythonprogram som frågar användaren efter en film, och skriv
     sedan ut en snygg infobox om filmen, typ så här:

*** Resultat från OMDB! ***
      Alien (1979) regisserades av Ridley Scott.
      Skådisar: Tom Skerritt, Sigourney Weaver, Veronica Cartwright, Harry Dean Stanton
    IMDB betyg: 8.4
        Awards: Won 1 Oscar. Another 16 wins & 22 nominations.
         Längd: 117 min
"""

import requests
from pprint import pprint

# land_before_time = "http://www.omdbapi.com/?t=Land+Before+Time&apikey=9f6d550c"

open_movie_db = "http://www.omdbapi.com/"
r = requests.get(open_movie_db, params={"t": "The Land Before Time", "apikey": "9f6d550c"})
data = r.json()
pprint(data)
