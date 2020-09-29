"""
20200929
Kristin
Uppgift 44

Lek med tuppler! (Tuples)
1. Bygg ett program som tar in användarens namn och ålder. Lagra resultatet i en tuppel (str, int).
Skicka tuppeln till en funktion, som skriver ut:
  Namn: <name>
  Ålder: <age>
.. ja ni fattar :)

2. Bygg en funktion som tar en tuppel med två tal som indata, och returnerar dessa i omvänd ordning. T.ex.
    t = (5, 6)
    print(swaptuple(t))
.. ska ge följande utskrift:
    (6, 5)

3. Bygg en funktion som tar in en lista ls, och returnerar en tuppel som bygger på listan. T.ex.
     print(to_tuple([1, 2, 3]))
... ska ge:
    (1, 2, 3)
"""


# 44.1
def user(user_info):
    user_name, user_age = user_info
    print(f"Name: {user_name}")
    print(f"Ålder: {user_age}")


name = "Ada"
age = 100
info = (name, age)
user(info)


# 44.2
def swap_tuple(t):
    (a, b) = t
    (a, b) = (b, a)
    t = (a, b)
    return t


one_two = (1, 2)
two_one = swap_tuple(one_two)
print(two_one)


# 44.3
def to_tuple(ls):
    return tuple(ls)


one_two_three = [1, 2, 3]
print(to_tuple(one_two_three))
