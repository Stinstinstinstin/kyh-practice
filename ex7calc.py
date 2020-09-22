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


def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    result = a / b
    return result
