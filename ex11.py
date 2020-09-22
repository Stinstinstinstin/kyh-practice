"""
20200922
Kristin
Uppgift 11

11.1 Ta en kopia på uppgift 9 och fixa programmet så att int(input(..)) inte kraschar om användaren skriver "abc"
(tips: använd try...except  block!)
11.2 Fortsätt jobba med det ni inte blev klara med i uppgift 9, 10
11.3 Jobba med extrauppgifter
"""

import random


def game():
    correct_answers = 0

    while True:
        try:
            number_of_questions = int(input("Hur många uppgifter vill du lösa? "))
            break
        except ValueError:
            print("U-hu! Du måste ange en siffra :)")

    while True:
        try:
            max_value = int(input("Hur stort får det största talet vara? "))
            break
        except ValueError:
            print("U-hu! Du måste ange en siffra :)")

    for i in range(number_of_questions):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)
        while True:
            try:
                answer = input(f"{a}+{b}=")
                number = int(answer)
                break
            except ValueError:
                print("Aj aj! Du måste ange ett tal :)")
        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
    print("---")
    print(f"Du fick {correct_answers} av {number_of_questions} rätt.")


if __name__ == '__main__':
    game()


