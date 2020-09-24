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


def read_file_and_print_on_screen(file_name):
    f = open(file_name, 'r')
    print("\n*** TODO list ***")
    for task_number, row in enumerate(f):
        print(task_number + 1, row.strip().capitalize())
    f.close()


def add_content_to_file(file_name, content):
    f = open(file_name, 'a')
    f.write(content.lower() + "\n")
    f.close()


def remove_task_from_file(file_name, task_to_remove):
    f = open(file_name, 'r')
    lines = f.readlines()

    f = open(file_name, 'w')
    for row_number, task in enumerate(lines):
        if row_number != int(task_to_remove) - 1:
            f.write(task.strip("\n") + "\n")
    f.close()


def main():

    while True:

        print("")
        print("1. Lista TODO")
        print("2. Lägg till en uppgift")
        print("3. Ta bort uppgift")
        print("4. Avbryt programmet")
        choice = int(input(">> "))

        if choice == 1:
            read_file_and_print_on_screen("ex17_todo.txt")

        elif choice == 2:
            new_task = input("Ny uppgift: ")
            add_content_to_file("ex17_todo.txt", new_task)
        elif choice == 3:
            print("Vilket uppgift vill du ta bort? (ange siffra)")
            task_to_remove = input(">>")
            remove_task_from_file("ex17_todo.txt", task_to_remove)
        elif choice == 4:
            print("\nProgrammet avslutas..")
            quit()
        else:
            print("\nFelaktigt val. Ange 1, 2, 3 eller 4.")
            continue


if __name__ == '__main__':
    main()
