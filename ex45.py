"""
20200930
Kristin
Uppgift 45

Vi har gått igenom "".format(..) och % (...) syntaxen. Här är en övning på detta!
1. Leta upp en tidigare lösning på en uppgift som innehåller f-strings.
Gör en kopia på filen, och byt alla f-strings mot .format. Jämför filerna. Vilken syntax föredrar ni?
2. Gör om samma övning fast byt till % (...) syntaxen.
3. Går det att göra motsvarande {xyz:20}  m.h.a format() eller % syntaxen? D.v.s att kräva ett v
isst antal tecken utrymme vid utskrift. Googla och läs på, experimentera!
4. Samma som (3), fast för vänster, höger, mittenjustering (d.v.s det vi gör med <, > och ^ i f-strings).
Tips: % tuple syntaxen är mycket lik printf i C/C++, så om du kan det så känner du igen dig.
T.ex. betyder %s sträng, och %d tal.
"""

import random

category1 = ["en dvärgflodhäst", "en skattkarta", "ett litet björndjur", "en rymdraket"]
category2 = ["köpas på ICA", "hittas i havet", "fångas på Mars", "hämtas i garaget"]
category3 = ["varna", "hjälpa", "skydda", "guida"]
category4 = ["precis kommit hem från en utlandsresa", "smittats med Corona", "har sovit mer än tre timmar per natt"]
category5 = ["Lillefot, Landet för längesedan", "John Thornton, Alaska", "Kilgore Trout, New York",
             "Spöket Laban, källaren på slottet Gomorronsol"]

val1 = category1[random.randrange(len(category1))]
val2 = category2[random.randrange(len(category2))]
val3 = category3[random.randrange(len(category3))]
val4 = category4[random.randrange(len(category4))]
val5 = category5[random.randrange(len(category5))]

# With f-strings
print("\nf-strings")
print(f"""{val1.capitalize()} som kan {val2} ska {val3}
finländare som kommit nära någon som
{val4}.
– Jag tycker att ni i Sverige borde överväga att göra något
liknande, säger {val5}.""")

# With .format(), specified width and left-/right-aligned
print("\n.format()")
print("""{val1:<20} som kan {val2:30} ska {val3}
finländare som kommit nära någon som
{val4:20}.
– Jag tycker att ni i Sverige borde överväga att göra något
liknande, säger {val5}.""".format(val1=val1.capitalize(), val2=val2, val3=val3, val4=val4, val5=val5))

# With %s %d %f, specified width and left-/right-aligned
print("\n%s %d %f")
print("""%-15s som kan %s ska %s
finländare som kommit nära någon som
%s.
– Jag tycker att ni i Sverige borde överväga att göra något
liknande, säger %s.""" % (val1.capitalize(), val2, val3, val4, val5))
