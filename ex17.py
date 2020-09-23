"""
20200923
Kristin
Uppgift 17

Bygg ett program där användaren ser denna meny:

1. Lista TODO
2. Lägg till uppgift
3. Ta bort uppgift
4. Avbryt programmet

Programmet ska spara en fil "TODO.txt" som läses in i början, och innehåller en lista med saker att göra.
Listan kan manipuleras med alternativ 2 och 3.

När programmet avslutas sparas listan till TODO.txt (skrivs över).

Detta är ett miniprojekt! Jag rekommenderar att ni fortsätter jobba tillsammans utanför lektionstid för att bli klara.
Diskutera hur ni ska lösa uppgiften först tillsammans.
"""


while True:

    print("")
    print("1. Lista TODO")
    print("2. Lägg till en uppgift")
    print("3. Ta bort uppgift")
    print("4. Avbryt programmet")
    choice = int(input("Ditt val: "))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("\nProgrammet avslutas..")
        quit()