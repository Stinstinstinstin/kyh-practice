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

# För att kunna köra filerna i mappen uppgift36 - högerklicka Mark Directory as Sources root
# Glöm inte lägga tillbaka root?
"""

from ex36_pwstrength import compute_strength

if __name__ == '__main__':

    while True:
        print("")
        password = input("Ange lösenord: ")
        print("")
        res, valid = compute_strength(password)
        if valid:
            if res == 0:
                print(f"Lösenordet får {res} poäng av 3. Svagt lösenord men godkänt.")
            if res == 1:
                print(f"Lösenordet får {res} poäng av 3.")
            if res > 1:
                print(f"Lösenordet får {res} poäng av 3. Bra lösenord!")
            break
        print("Ogiltligt lösenord! Försök igen!")
