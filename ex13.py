"""
20200923
Kristin
Uppgift 13
Skriv ett program tillsammans, from scratch!

Copy-pastat från en stor svensk tidning, ingressen till en nyhetsartikel:

En app som kan laddas ned till mobiltelefonen ska varna
finländare som kommit nära någon som smittats med
coronaviruset.
– Jag tycker att ni i Sverige borde överväga att göra något
liknande, säger Markku Tervahauta, generaldirektör för
Finska institutet för hälsa och välfärd, THL.

Byt ut minst 4 ord/uttryck till slumpade ord/uttryck från 4 kategorier, och skriv ut resultatet.
Varje kategori ska ha minst 2 ord, gärna fler! Var kreativa...

Exempel output (välj själva vilka ord/uttryck som ska bytas ut!)

En app som kan beställas på posten ska varna skåningar som chattat med någon som smittats av vattkoppor.
- Du tycker att vi i Helsingland borde strunta i att göra något liknande, säger Jonathan, chef för Svenska institutet
för inre säkerhet, SIIS.

Utbytt:
   laddas ned till mobiltelefonen -> beställas på posten
   finländare -> skåningar
   kommit nära -> chattat med
   coronaviruset -> vattkoppor
   Jag -> Du
   ni -> vi
   Sverige -> Helsingland
   överväga -> strunta i
   Markku Tervahauta -> Jonathan
   generaldirektör -> chef
   Finska institutet för hälsa och välfärd, THL -> Svenska institutet för inre säkerhet, SIIS

Tips på bra-att-ha grejer i Python:
  * randint
  * list-access (min_lista[0] hämtar första elementet, t.ex.)
  * längd på listor (len)
  * f-strings
"""

import random

category1 = ["en dvärgflodhäst", "en skattkarta", "ett litet björndjur", "en rymdraket"]
category2 = ["köpas på ICA", "hittas i havet", "fångas på Mars", "hämtas i garaget"]
category3 = ["varna", "hjälpa", "skydda", "guida"]
category4 = ["precis kommit hem från en utlandsresa", "smittats med Corona", "har sovit mer än tre timmar per natt"]
category5 = ["Lillefot, Landet för längesedan", "John Thornton, Alaska", "Kilgore Trout, New York", "Spöket Laban, källaren på slottet Gomorronsol"]

val1 = category1[random.randrange(len(category1))]
val2 = category2[random.randrange(len(category2))]
val3 = category3[random.randrange(len(category3))]
val4 = category4[random.randrange(len(category4))]
val5 = category5[random.randrange(len(category5))]


print(f"""\n{val1.capitalize()} som kan {val2} ska {val3}
finländare som kommit nära någon som 
{val4}.
– Jag tycker att ni i Sverige borde överväga att göra något
liknande, säger {val5}.""")

