"""
20200927
Kristin
Uppgift 35

En övning på POST-requests.

Spara bifogad fil i en fil ex35_quizzservice.py först av allt!

35.1 Undersök filen och försök förstå vad den gör. Diskutera i gruppen.

35.2 I ex35_quizzservice.py syns ??? två gånger. Googla efter hur man POSTar JSON
     med hjälp av requests och fyll i på båda ställena!

35.3 Bygg ett pythonscript som skriver ut hur många frågor som finns i quizz-db.

35.4 Utöka scriptet så att följande meny likt syns:

   Det finns 3 frågor i quizz-db. Gör ett val:
   1. Lägg till fråga
   2. Avsluta programmet

Val 1 ger användaren följande frågor:

   Skriv en fråga: bla bla bla
   Vad är rätt svar: bla bla bla
   Ange några felaktiga svar (separera dem med kommateckan): bla,bla,bla
   Tack för ditt bidrag!

.. och sedan kommer hen tillbaka till huvudmenyn.

"""

import ex35_quizzservice


def main():

    api = ex35_quizzservice.QuizzWebServiceAPI()
    while True:
        questions = api.get_all_questions()
        print("")
        print(f"Det finns {len(questions)} frågor i quizz-db. Gör ett val: ")
        print("1. Lägg till fråga")
        print("2. Avsluta programmet")
        choice = input(">> ")

        if choice == "1":
            print("")
            question = input("Skriv frågan du vill lägga till: ")
            correct_answer = input("Skriv rätt svar: ")
            wrong_answer1 = input("Skriv första felaktiga svaret: ")
            wrong_answer2 = input("Skriv andra felaktiga svaret: ")
            wrong_answers = [wrong_answer1, wrong_answer2]
            api.add_question(question, correct_answer, wrong_answers)
            print("Tack! Din fråga är nu inlagd. :)")

        elif choice == "2":
            print("Programmet avslutas..")
            quit()

        else:
            print("Ogiltligt val. Välj 1 eller 2. ")


if __name__ == '__main__':
    main()
