"""
20200922
Kristin
Uppgift 7
Glöm inte testa och committa mellan varje uppgift.

7.1 Skapa en ny modul ( = fil ) som heter calc.py,
och flytta först bara "add"-funktionen dit. Använd calc.add i huvudprogrammet
7.2 I PyCharm finns det något som kallas "Move".
Högerklicka på "sub" välj Refactor->Move, följ instruktionerna och flytta funktionen till calc.
7.3 Flytta resten till calc
"""

from ex7calc import add, subtract, multiply, divide


def run():
    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    print("3 - multiply numbers")
    print("4 - divide numbers")
    answer = input(">> ")
    a = int(input("A="))
    b = int(input("B="))
    if answer == "1":
        result = add(a, b)
    if answer == "2":
        result = subtract(a, b)
    if answer == "3":
        result = multiply(a, b)
    if answer == "4":
        result = divide(a, b)

    print(f"Result = {result}")


if __name__ == '__main__':
    run()
