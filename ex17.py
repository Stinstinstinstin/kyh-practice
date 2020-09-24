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


def read_file(file_name):
    f = open(file_name, 'r')
    print("\n__This is your TODO list__")
    for row in f:
        print(row.rstrip())
    f.close()


def write_to_file(file_name, content):
    f = open(file_name, 'a')
    f.write(content + "\n")
    f.close()


def main():

    while True:

        print("")
        print("1. Lista TODO")
        print("2. Lägg till en uppgift")
        print("3. Ta bort uppgift")
        print("4. Avbryt programmet")
        choice = int(input("Ditt val: "))

        if choice == 1:
            read_file("ex17_todo.txt")

        elif choice == 2:
            new_task = input("Ny uppgift: ")
            write_to_file("ex17_todo.txt", new_task)
        elif choice == 3:
            pass
        elif choice == 4:
            print("\nProgrammet avslutas..")
            quit()


if __name__ == '__main__':
    main()
