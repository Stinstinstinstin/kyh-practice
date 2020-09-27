"""
20200927
Kristin
Uppgift 36

Vi ska öva lite på att dela upp program i moduler!

Skapa en mapp i erat kyh-practice som heter "uppgift36".
I den mappen, som blir vår "app", skapa två Pythonscript:

    ex36_main.py   # huvudprogrammet som ni kör
    ex36_pwstrength.py  # en hjälpmodul som main använder sig av

ex36_main.py ska fråga användaren efter ett lösenord, och anropa en funktion compute_strength(pw)
[som ska bo i ex36_pwstrength.py] som ger ut ett värde 0-3 beroende på följande regler:

  a) om lösenordet är mer än 10 tecken långt får det +1 poäng
  b) om lösenordet innehåller både siffror och bokstäver (det räcker med de engelska bokstäverna) så får det +1 poäng
  c) om lösenordet innehåller någon av symbolerna “#%&+_-” får det +1 poäng
  d) om lösenordet innehåller något annat tecken än bokstäver, siffror och symbolerna i (3) är det ogiltigt och får 0 poäng.

Tips - None kan användas för att beskriva ogiltigt lösenord, fall (d).

Lägg tillbaka root!
"""


def compute_strength(pw):
    num_points = 0
    valid = True

    # a) om lösenordet är mer än 10 tecken långt får det +1 poäng
    if len(pw) > 10:
        num_points += 1

    # b) om lösenordet innehåller både siffror och bokstäver (det räcker med de engelska bokstäverna)
    # så får det +1 poäng
    if any(char.isdigit() for char in pw):
        if any(char.isalpha() for char in pw):
            num_points += 1

    # c) om lösenordet innehåller någon av symbolerna “#%&+_-” får det +1 poäng
    special_characters = "#%&+_-"
    if any(char in special_characters for char in pw):
        num_points += 1

    # d) om lösenordet innehåller något annat tecken än bokstäver, siffror och symbolerna i (3)
    # är det ogiltigt och får 0 poäng.
    if not (any(char.isdigit() for char in pw)
            or any(char.isalpha() for char in pw)
            or any(char in special_characters for char in pw)):
        num_points = 0
        valid = False

    return num_points, valid
