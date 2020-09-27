"""
20200922
Kristin
Uppgift 10

Skriv flera program (t.ex ug10_1.py, ug10_2.py osv) som skriver ut:
1) heltalen fr.o.m. 1 t.o.m. 10 i ökande ordning
2) udda tal fr.o.m. 1 t.o.m. 49 i ökande ordning
3) heltal fr.o.m. 10 t.o.m. 1 i minskande ordning
4) summan av talen 7 t.o.m 1000
5) produkten av talen 1 t.o.m 1000
"""

print("\nSumman av talen 7 tom 1000")
print("____+=____")
summa = 0
for i in range(7, 1000+1):
    summa += i
print(summa)

print("____sum(range()____")
print(sum(range(7, 1000+1)))

print("____sum()____")
ls = []
for i in range(7, 1000+1):
    ls.append(i)
print(sum(ls))
