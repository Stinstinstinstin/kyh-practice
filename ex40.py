"""
20200926
Kristin
Uppgift 40

1. Skriv en funktion om "vänder" en textsträng baklänges - utan att använda "reverse" (eller [::-1])!
Använd istället strängar eller listor, och en for-loop.
T.ex. "12345" blir "54321".

2. Skriv en funktion som tar in en textsträng, och returnerar antalet stora bokstäver i strängen.

3. Skriv en funktion som avgör om ett tal ligger mellan två andra tal.
t.ex.
  inrange(value=1, min=2, max=3) blir False eftersom 1 ligger utan för 2 till 3.
  inrange(value=10, min=0, max=100) blir True eftersom 10 ligger mellan 0 och 100.
"""

print("1. Skriv en funktion om 'vänder' en textsträng baklänges - utan att använda 'reverse' (eller [::-1])!")


def reverse_text(text):
    new_text = ""
    for letter in text:
        new_text = letter + new_text
    return new_text


text = "abcdefgh"
rev_text = reverse_text(text)
print(rev_text)

print("2. Skriv en funktion som tar in en textsträng, och returnerar antalet stora bokstäver i strängen.")


def check_if_upper(text):
    number_of_capitals = 0
    for letter in text:
        if letter.isupper():
            number_of_capitals += 1
    return number_of_capitals


alphabet = "Abc DeF"
print(alphabet)
print(f"Antal versaler: {check_if_upper(alphabet)}")

print("3. Skriv en funktion som avgör om ett tal ligger mellan två andra tal.")


def check_integer_relation(a, b, c):
    if b < a < c or c < a < b:
        return True
    else:
        return False


print(check_integer_relation(4, 5, 5))
