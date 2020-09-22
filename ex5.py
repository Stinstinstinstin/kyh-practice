"""
20200922
Kristin
Uppgift 5
Vi har gått igenom funktioner i teorin, nu blir det praktik!

1. Ändra så att hela while-loopen ligger i en funktion som heter "mainloop",
och testa så att programmet fungerar fortfarande.
2. Bygg en funktion "ask_number" som returnerar ett heltal som användaren matar in.
3. Ändra på mainloop så att den returnerar antal gissningar användaren använt sig av,
och skriv ut antalet utanför mainloop, inte  inuti.
def ask_number():
    text = input("Vad är din gissning?")
    tal = int(text)
    return tal
"""

import random

n = random.randint(1, 100)


def ask_number():
    text = input("Vad är din gissning? ")
    tal = int(text)
    return tal


def mainloop():
    antal_gissningar = 0
    while True:
        as_number = ask_number()

        antal_gissningar += 1
        if as_number == n:
            print(f"\nKorrekt! {as_number} var rätt nummer!")
            break

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")

    return antal_gissningar


if __name__ == "__main__":
    print("Jag tänker på ett tal mellan 1 och 100.")
    antal_gissningar = mainloop()
    print(f"Du gissade rätt på {antal_gissningar} försök :)")




