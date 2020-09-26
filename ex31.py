"""
20200926
Kristin
Uppgift 31
Ta en kopia på lösningen av uppgift 30!

31.1 I nya filen, byt ut for-loopar mot list-comprehensions så mycket ni kan.
     Jämför de två filerna, vilken tycker ni är mest läsbar/enklast att förstå?

31.2 Utöka 30.2 med följande utskrifter:

    Udda tal: 1, 3, 5
    Jämna tal: 2, 100


Tips: det går att skriva if-uttryck i list-comprehensions! Googla och härma!
"""

# registration_number = input("Ange regnr: ")
# letters = registration_number[0:3]
# numbers = registration_number[3:6]
#
# print(f"Bokstävsgrupp: {letters}")
# print(f"Siffergrupp: {numbers}")

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
# reversed_numbers = str(number[::-1]).replace('[', '').replace(']', '')
reversed_numbers = [str(i) for i in number[::-1]]
print(f"Talen baklänges: {', '.join(reversed_numbers)}")

# reversed()
reversed_numbers2 = [str(i) for i in list(reversed(number))]
print(f"Talen baklänges: {', '.join(reversed_numbers2)}")

odd_numbers = [str(i) for i in number if i % 2 != 0]
even_numbers = [str(i) for i in number if i % 2 == 0]

print(f"Udda tal: {', '.join(odd_numbers)}")
print(f"Jämna tal: {', '.join(even_numbers)}")
