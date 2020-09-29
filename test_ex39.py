"""
Uppgift 42

1. Lägg till minst 3 enhetstester för funktionen ni byggde i uppgift 39.1.
2. Upprepa för 39.2
3. Upprepa för 39.3

"""

from ex39 import calc_max, calc_sum, calc_product

# calc max
def test_calc_max():
    expected = 3
    got = calc_max(1, 2, 3)
    assert expected == got


def test_calc_max_equal_input():
    assert calc_max(1, 1, 1) == 1


def test_calc_max_2():
    assert calc_max(100, 200, 300) == 300


# calc sum
def test_calc_sum_equal_input():
    expected = 3
    got = calc_sum([1, 1, 1])
    assert expected == got


def test_calc_sum():
    assert calc_sum([100, 200, 300]) == 600


def test_calc_sum_zero_input():
    assert calc_sum([0]) == 0


def test_calc_sum_zero_inputs():
    assert calc_sum([0, 0, 0, 0, 0, 0]) == 0


# calc product
def test_calc_product_equal_input():
    expected = 1
    got = calc_product([1, 1, 1])
    assert expected == got


def test_calc_product():
    assert calc_product([1, 2, 3]) == 6


def test_calc_product_zero_input():
    assert calc_product([0, 0, 2, 3]) == 0
