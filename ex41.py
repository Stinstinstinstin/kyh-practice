"""
20200929
Kristin
Uppgift 41

Klona mitt kyh-practice repo (eller uppdatera om ni redan har det på datorn): https://github.com/objarni/kyh-practice
I det hittar ni en fil "scope1.py".
1. Läs igenom koden UTAN ATT KÖRA DEN och diskutera vad som kommer skrivas ut tillsammans. Tycker alla samma sak?
2. Kör nu koden, och undersök output. Blev det enligt förväntan? Diskutera!
"""

a = 1
def fn():
    global a
    print(a)
    a = 2
    print(a)

print(a)
fn()
print(a)

# 1
# 1
# 2
# 1

