"""
20200926
Kristin
Uppgift 30
Träna slicing av strängar och listor!

Reg.nr på bilar i Sverge skrivs traditionellt* med tre bokstäver och tre siffror.

1. Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
var för sig; använd slicing-syntax för att dela upp inputsträngen.

Ex.

Ange regnr: ABC663
Bokstävsgrupp: ABC
Siffergrupp: 663

2. Bygg ett program där användaren matar in ett gäng heltal med komma emellan, och skriver ut följande:
    Ange tal med komma emellan: 1,2,3,5,100
    Första talet: 1
    Sista talet: 100
    Summan av talen: 111
    Talen baklänges: 100, 5, 3, 2, 1

Tips: Använd slicing och inbyggda funktionen sum().
Tips 2: Det går att lösa "Talen baklänges" på två sätt: det lätta sättet
   är med inbyggda funktionen reverse(). Det svåra sättet är med slicing syntax!
   Pröva båda :)

*numera kan det vara bokstäver i sifferdelen också. Det gör ont att se men det är moderna tider!
"""

# 30.1
registration_number = input("Ange regnr: ")
letters = registration_number[0:3]
numbers = registration_number[3:6]

print(f"Bokstävsgrupp: {letters}")
print(f"Siffergrupp: {numbers}")

# 30.2
number = input("Ange tal med komma emellan: ")
number = number.split(',')
first_number = number[0]
last_number = number[-1]
print(f"Första talet: {first_number}")
print(f"Sista talet: {last_number}")

number = [int(i) for i in number]
summa = sum(number)
print(f"Summan av talen: {summa}")


# [ <first element to include> : <first element to exclude> : <step> ]
reversed_numbers = str(number[::-1]).replace('[', '').replace(']', '')
print(f"Talen baklänges: {reversed_numbers}")

reversed_numbers2 = str(list(reversed(number))).replace('[', '').replace(']', '')
print(f"Talen baklänges: {reversed_numbers2}")

