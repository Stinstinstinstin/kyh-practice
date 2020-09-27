"""
20200927
Kristin
Uppgift 32
Skriv ett Pythonprogram som tar in en sträng från användaren, och skriver ut följande:

32.1 Längden på strängen
32.2 Om strängen är ett "palindrom" eller ej. Exempel på palindrom: rattar, Ebbe.
Observera att programmet ska klara att användaren blandar stora och små bokstäver!
32.3 Utöka programmet så att även uttryck som "Aja Baja" anses vara palindrom,
d.v.s filtrera bort alla mellanslag ifrån inputsträngen!

Tips: använd det vi lärde oss igår kring att vända en sträng och/eller lista baklänges,
och join-funktionen. Även list comprehension kan komma till användning.
"""

# Accepterar "Aja, baja" som palindrom
print("\nExempel 1")
text = input("Skriv något: ")

text_only_alpha = [char for char in text.lower() if char.isalpha()]
reversed_text_only_alpha = text_only_alpha[::-1]

if text_only_alpha == reversed_text_only_alpha:
    print(f"{text} är ett palindrom!")
else:
    print("Ej palindrom.")

print(f"(Texten är {len(text)} tecken lång)")


# Kodlösning från föreläsning
# Accepterar inte "Aja, baja" som palindrom
print("\nExempel 2")
text = input("Skriv något: ")

lowercase = ''.join([c for c in text.lower() if c != ' '])
lowercase_rev = lowercase[::-1]

if lowercase == lowercase_rev:
    print(f"{text} är ett palindrom!")
else:
    print("Ej palindrom.")

print(f"(Texten är {len(text)} tecken lång)")
