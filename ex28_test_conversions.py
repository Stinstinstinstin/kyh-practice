"""
20200926
Kristin
Uppgift 28
Nedan ser ni 2 enhetstester för konvertering mellan olika enheter.
Spara testerna i en fil kallad "test_conversions.py".
Utöka "requirements.txt" med en rad som innehåller "pytest" -
detta är ett mycket populärt verktyg för att köra automatiska tester i Python.

# test_conversions.py
from conversions import m_to_mm, cm_to_m

def test_conversion_from_meters_to_mm():
    expected = 1000
    got = m_to_mm(m=1)
    assert expected == got

def test_cm_to_m():
    expected = 2
    got = cm_to_m(cm=200)
    assert expected == got

28.1 Implementera funktionerna m_to_mm och cm_to_m i en ny modul conversions.py.
28.2 Lägg till några fler tester för m_to_mm med andra värden, så att ni är helt
     säkra på att funktionerna fungerar som de ska!
28.3 Skriv 2 tester för en ny funktion mm_to_m (som inte finns än).
28.4 Implementera funktionen conversions.mm_to_m!
28.5 Skriv tillräckligt många tester för att ni ska känna att ni litar på en funktion
     som konverterar från Fahrenheit till Celsius. Hur många tester räcker? Diskutera!
"""

# test_conversions.py
from ex28_conversions import m_to_mm, cm_to_m, mm_to_m, fahrenheit_to_celsius


# m to mm
def test_conversions_m_to_mm():
    expected = 1000
    got = m_to_mm(length_in_meter=1)
    assert expected == got


def test_conversions_m_to_mm_zero_input():
    expected = 0
    got = m_to_mm(length_in_meter=0)
    assert expected == got


def test_conversions_m_to_mm_decimal_input():
    expected = 1500
    got = m_to_mm(length_in_meter=1.5)
    assert expected == got


def test_conversions_m_to_mm_reverse():
    expected = 1
    got = m_to_mm(length_in_meter=1000)
    assert expected != got


# cm to m
def test_conversions_cm_to_m():
    expected = 2
    got = cm_to_m(length_in_centimeter=200)
    assert expected == got


def test_conversions_cm_to_m_zero_input():
    expected = 0
    got = cm_to_m(length_in_centimeter=0)
    assert expected == got


def test_conversions_cm_to_m_decimal_input():
    expected = 0.015
    got = cm_to_m(length_in_centimeter=1.5)
    assert expected == got


def test_conversions_cm_to_m_reverse():
    expected = 200
    got = cm_to_m(length_in_centimeter=2)
    assert expected != got


# mm to m
def test_conversions_mm_to_m():
    expected = 1
    got = mm_to_m(length_in_mm=1000)
    assert expected == got


def test_conversions_mm_to_m_zero_input():
    expected = 0
    got = mm_to_m(length_in_mm=0)
    assert expected == got


def test_conversions_mm_to_m_decimal_input():
    expected = 0.0015
    got = mm_to_m(length_in_mm=1.5)
    assert expected == got


def test_conversions_mm_to_m_reverse():
    expected = 1000
    got = mm_to_m(length_in_mm=1)
    assert expected != got


# fahrenheit to celsius
def test_conversions_fahrenheit_to_celsius():
    expected = -17.222
    got = fahrenheit_to_celsius(temp_in_fahrenheit=1)
    assert expected == got


def test_conversions_fahrenheit_to_celsius_zero_expected():
    expected = 0
    got = fahrenheit_to_celsius(temp_in_fahrenheit=32)
    assert expected == got


def test_conversions_fahrenheit_to_celsius_zero_input():
    expected = -17.778
    got = fahrenheit_to_celsius(temp_in_fahrenheit=0)
    assert expected == got


def test_conversions_fahrenheit_to_celsius_negative_input():
    expected = -23.333
    got = fahrenheit_to_celsius(temp_in_fahrenheit=-10)
    assert expected == got


def test_conversions_fahrenheit_to_celsius_decimal_input():
    tolerance = 0.001
    expected = -16.944
    got = fahrenheit_to_celsius(temp_in_fahrenheit=1.5)
    assert got - tolerance <= expected <= got + tolerance
