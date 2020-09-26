"""
20200926
Kristin
Uppgift 25
Fortsättning på uppgift 24 - mer om JSON och requests (webapi-anrop).

Nu ska vi bearbeta datan något med hjälp av Python och f-string tricken jag visade er!

25.1 Skriv ett Pythonprogram som använder requests mot URLen ni fick i uppgift 24,
och skriver ut kurstillfällen som sker under oktober 2020, på denna form:

   Kursnamn: Professional Scrum Product Owner (EN), 15-16 september, Stockholm
 Startdatum: 2020-10-15
   Slutdatum: 2020-10-17

   Kursnamn: Professional Scrum Master, 15-16 september, Stockholm
 Startdatum: 2020-10-15
   Slutdatum: 2020-10-16

Den första kolumnen, fram till och med ":" är 12 tecken bred, och högerställd.
Den andra kolumen är 100 tecken bred, och vänsterställd.

25.2 Istället för att hårdkoda oktober 2020 just, låt användaren mata in ett år och en månad,
som ni sedan använder för att filtrera ut kurserna som skrivs ut! T.ex.

   Year: 2020
   Month (1-12): 12
   Searching for courses in date range 2020-12-01 to 2020-12-31

Tips: det går bra att använda -01 och -31 för att inkludera hela månaden,
även om vissa månader inte har så många dagar!

"""

import requests


def main():

    r = requests.get('https://proagile.se/api/publicEvents')
    data = r.json()

    print("\nSök efter kurs som startar ett visst datum\n")
    year = input("År (2020-2022): ")
    month = input("Månad (01-12): ")
    print(f"Letar efter kurser som startar någon gång {year}-{month}-01 till {year}-{month}-31\n")

    found_course = False
    for i in range(len(data)):
        course = data[i]['courseName']
        start_date = data[i]['startDate']
        end_date = data[i]['endDate']

        if start_date[0:4] == year and start_date[5:7] == month:
            print("")
            print(f'{"Kursnamn:":>12} {course:<100}')
            print(f'{"Startdatum:":>12} {start_date:<100}')
            print(f'{"Slutdatum:":>12} {end_date:<100}')
            found_course = True
    if not found_course:
        print("Hittade tyvärr inga kurser.")


if __name__ == '__main__':
    main()
