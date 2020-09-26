"""
20200926
Kristin
Uppgift 23

Den här uppgift går ut på att träna "exploratory testing", d.v.s att man prövar hur något system/API/program fungerar
genom att helt enkelt experimentera på ett systematiskt och kreativt sätt!

Vanligast är att testa ett användargränssnitt (UI/webbsida/system) som en användare, men i denna kurs lär vi oss
programmering, så vi testa att försöka ta isär en inbyggd funktion! :)

Vi har alla sett funktionen som delar upp strängar i listor av strängar: split(), t.ex:

   "abc,def,ghi".split(",") ---> ["abc", "def", "ghi"]

Nu är er uppgift att hitta alla sätt som får split att "krasha" eller på annat sätt bete sig underligt.
Pröva helt enkelt att skicka in "fel sorts argument", och samla ihop så många Exceptions
(och annat udda beteende) som ni kan hitta!

Tips: Använd Python Console för att pröva snabbt. Dokumentera vad du hittar i split-observations.txt i ditt
kyh-practice repo.

"""

test = "         1 2     3 "
print(f"\nOriginal: {test}")

test_split = test.split()
print(f"\nEfter .split(): {test_split}")

"""
Hittar följande fel:

- AttributeError: 'int' object has no attribute 'split' (test = 1)
    test = 1
    1.split()
- AttributeError: 'list' object has no attribute 'split' (test = ["a, b", "c"])
    ["a", "b c"].split()
- TypeError: must be str or None, not int ("a b c".split(1))
    "a b c".split(1)
- TypeError: must be str or None, noot bool ("a b c".split(True))
    "a b c".split(True)
- SyntaxError: invalid syntax (1.split())
    1.split()
- ValueError: empty separator ("a,b,c".split(''))
    "a,b,c".split('')
"""