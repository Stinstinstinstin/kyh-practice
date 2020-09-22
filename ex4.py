"""
20200922
Kristin
Uppgift 4
Genomför följande ändringar.

1. Fråga efter tal mellan 1 och 100 istället.
2. Översätt programmet till svenska!
3. Lägg till en ny variabel "antal_gissningar",
som håller reda på hur många gissningar användaren behövde
för att hitta talet. Skriv ut hur många gissningar efteråt.
"""

import random

antal_gissningar = 0
n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilket?")

while True:
    text = input("Din gissning: ")
    as_number = int(text)

    antal_gissningar += 1
    if as_number == n:
        print(f"\nKorrekt! {as_number} var rätt nummer!")
        print(f"Du gissade rätt på {antal_gissningar} försök :)")
        break

    if as_number < n:
        print("Fel, mitt nummer är högre... Försök igen!")

    if as_number > n:
        print("Fel, mitt nummer är lägre... Försök igen!")
