"""
20200923
Kristin
Uppgift 15

Ett litet potpurri av småproblem att lösa tillsammans!

15.1 Implementera "wordcount" som jag och Christoffer byggde
15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com) och skriv ut hur många vokaler
som finns i strängen. Tips: "a" in "abcd" är True!
15.3 Göteborgsvarvet, vilken placering kom XYZ på? Implementera resten av detta program:
    runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
    vem = input(“Ange löpare du söker placering för”)
"""
#15.1 ?

#15.2
lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

vowels = ['a', 'e', 'i', 'o', 'u']

number_of_vowels = 0
for letter in lorem_ipsum.lower():
    if letter in vowels:
        number_of_vowels += 1
print("\n---------------------------")
print(f"Number of vowels: {number_of_vowels}")

found_vowels = [letter for letter in lorem_ipsum.lower() if letter in vowels]
print("---------------------------")
print(f"Number of vowels: {len(found_vowels)}")
print("---------------------------")

#15.3
print("Resultat på Göteborgsvarvet!")
runners_in_order = "Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus".split()
runner = input("Ange löpare du sökte placering för: ").capitalize()
order = runners_in_order.index(runner) + 1
print(f"{runner} kom på plats {order}")

