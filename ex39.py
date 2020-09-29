"""
20200926
Kristin
Uppgift 39

Repetition och träning på funktioner!
1. Skriv en funktion som beräknar maximum (=största värdet) av tre tal
2. Skriv en funktion som summerar alla tal i en lista. Inbyggda funktionen sum() ska ej användas
3. Skriv en funktion som räknar ut produkten (=multiplikation av alla tal) av en lista av heltal
"""

print("1. Skriv en funktion som beräknar maximum (=största värdet) av tre tal")


# Notera att: a > (b and c) inte är en hit ;) Inte heller en catch all else >_<
def calc_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


max_value = calc_max(5, 8, 8)
print(max_value)


def calc_max2(a, b, c):
    biggest = a
    if biggest < b:
        biggest = b
    if biggest < c:
        biggest = c
    return biggest

print("2. Skriv en funktion som summerar alla tal i en lista. Inbyggda funktionen sum() ska ej användas")
some_numbers = [10, 1, 9]


def calc_sum(values):
    summa = 0
    for value in values:
        summa += value
    return summa


sum_of_values = calc_sum([1, 2, 3])
print(sum_of_values)

print(calc_sum(some_numbers))

print("3. Skriv en funktion som räknar ut produkten (=multiplikation av alla tal) av en lista av heltal")


def calc_product(values):
    product = 1
    for value in values:
        product *= value
    return product


product_of_values = calc_product([1, 2, 3])
print(product_of_values)

print(calc_product(some_numbers))
