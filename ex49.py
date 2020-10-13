"""
49
1. Diskutera: Vad kommer stå i terminalen när man kör programmet?
2. Beskriv vad raderna 34-36 gör för varandra! Beskriv flödet i programmet,
mellan klasserna och funktionen, rad-för-rad. Använd begrepp som klass,
objekt/instans, konstruktor/init, funktion, metod, variabel.
Försök använda så många ord som möjligt, och vara så onödigt detaljerade ni bara kan!
Författa en beskrivning tillsammans och posta som kommentar till denna uppgift här i Google Classroom.
3. Utöka programmet med de två TODO som ligger med i programmet.
"""

# Förståelse kring objektorientering genom djur och deras läten, egenskaper
import random


class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Woff!")

    def make_trick(self):
        tricks = ['roll', 'sit', 'jump']
        print(f"{self.name}: making trick {random.choice(tricks)}")


class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Mjau!")

    def make_trick(self):
        print(f"{self.name}: Cat's don't make tricks on demand!")



class Parrot:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Polly wants a cracker!")

    def make_trick(self):
        tricks = ['whistle', 'steal a cracker', 'jump']
        print(f"{self.name}: making trick {random.choice(tricks)}")


def play_with_animals():
    hund = Dog("Rufus")
    hund.make_sound()
    hund.make_trick()
    cat = Cat("Cecilia")
    cat.make_sound()
    cat.make_trick()
    parrot = Parrot("Polly")
    parrot.make_sound()
    parrot.make_trick()


if __name__ == '__main__':
    play_with_animals()