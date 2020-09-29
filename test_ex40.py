"""
Uppgift 43
Likt uppgift 42, skriv enhetstester för funktionerna från uppgift 40.
"""

from ex40 import reverse_text, check_if_upper, check_integer_relation


def test_reverse_text():
    assert reverse_text("abc") == "cba"

def test_reverse_text_with_space():
    assert reverse_text("abc def") == "fed cba"

def test_reverse_text_empty():
    assert reverse_text("") == ""

def test_reverse_text_special_chars():
    assert reverse_text("abc&'") == "'&cba"

def test_check_if_upper():
    assert check_if_upper("Abc") == 1

def test_check_if_upper_more_than_one():
    assert check_if_upper("Abc DEF") == 4

def test_check_if_upper_letters_numbers():
    assert check_if_upper("Abc12") == 1

def test_check_if_upper_empty():
    assert check_if_upper("") == 0

def test_check_integer_relation():
    assert check_integer_relation(2, 1, 3) == True

def test_check_integer_relation_wrong_params():
    assert check_integer_relation(2, 3, 1) == False

def test_check_integer_relation_same_value():
    assert check_integer_relation(1, 1, 1) == False

def test_check_integer_relation_same_value_not_true():
    assert check_integer_relation(1, 1, 1) != True

def test_check_integer_relation_same_values_zero():
    assert check_integer_relation(0, 0, 0) == False

def test_check_integer_relation_negative_value():
    assert check_integer_relation(-10, -20, 0) == True