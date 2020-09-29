"""
20200929
Kristin
Uppgift 42

1. Lägg till minst 3 enhetstester för funktionen ni byggde i uppgift 39.1.
2. Upprepa för 39.2
3. Upprepa för 39.3
"""

from ex39 import calc_max, calc_max2, calc_sum, calc_product


# calc max
def test_calc_max_first_pos():
    expected = 3
    got = calc_max(3, 2, 1)
    assert expected == got


def test_calc_max_middle_pos():
    expected = 3
    got = calc_max(1, 3, 2)
    assert expected == got


def test_calc_max_last_pos():
    expected = 3
    got = calc_max(1, 2, 3)
    assert expected == got


def test_calc_max_equal_input():
    assert calc_max(1, 1, 1) == 1


def test_calc_max_equal_input_pos_0_1_lower():
    assert calc_max(1, 1, 9) == 9


def test_calc_max_equal_input_pos_1_2_lower():
    assert calc_max(9, 1, 1) == 9


def test_calc_max_equal_input_pos_0_2_lower():
    assert calc_max(1, 9, 1) == 9


def test_calc_max_equal_input_pos_0_1_higher():
    assert calc_max(9, 9, 1) == 9


def test_calc_max_equal_input_pos_1_2_higher():
    assert calc_max(1, 9, 9) == 9


def test_calc_max_equal_input_pos_0_2_higher():
    assert calc_max(9, 1, 9) == 9


def test_calc_max_zero_input():
    assert calc_max(0, 0, 0) == 0


def test_calc_max_negative_input():
    assert calc_max(-10, -10, -20) == -10


# calc max 2
def test_calc_max2_first_pos():
    expected = 3
    got = calc_max2(3, 2, 1)
    assert expected == got


def test_calc_max2_middle_pos():
    expected = 3
    got = calc_max2(1, 3, 2)
    assert expected == got


def test_calc_max2_last_pos():
    expected = 3
    got = calc_max2(1, 2, 3)
    assert expected == got


def test_calc_max2_equal_input():
    assert calc_max2(1, 1, 1) == 1


def test_calc_max2_equal_input_pos_0_1_lower():
    assert calc_max2(1, 1, 9) == 9


def test_calc_max2_equal_input_pos_1_2_lower():
    assert calc_max2(9, 1, 1) == 9


def test_calc_max2_equal_input_pos_0_2_lower():
    assert calc_max2(1, 9, 1) == 9


def test_calc_max2_equal_input_pos_0_1_higher():
    assert calc_max2(9, 9, 1) == 9


def test_calc_max2_equal_input_pos_1_2_higher():
    assert calc_max2(1, 9, 9) == 9


def test_calc_max2_equal_input_pos_0_2_higher():
    assert calc_max2(9, 1, 9) == 9


def test_calc_max2_zero_input():
    assert calc_max2(0, 0, 0) == 0


def test_calc_max2_negative_input():
    assert calc_max2(-10, -10, -20) == -10


# calc sum
def test_calc_sum():
    assert calc_sum([100, 200, 300]) == 600


def test_calc_sum_equal_input():
    expected = 3
    got = calc_sum([1, 1, 1])
    assert expected == got


def test_calc_sum_zero_input():
    assert calc_sum([0]) == 0


def test_calc_sum_zero_inputs():
    assert calc_sum([0, 0, 0, 0]) == 0


def test_calc_sum_negative_inputs():
    assert calc_sum([-1, -1, -1, -1]) == -4


# calc product
def test_calc_product():
    assert calc_product([1, 2, 3]) == 6


def test_calc_product_equal_input():
    expected = 1
    got = calc_product([1, 1, 1])
    assert expected == got


def test_calc_product_zero_input():
    assert calc_product([0, 0, 2, 3]) == 0


def test_calc_product_negative_input():
    assert calc_product([-1, 2, 3]) == -6
