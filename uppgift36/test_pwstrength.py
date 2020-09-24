from pwstrength import compute_strength


def test_password_with_length_11_gives_1_point():
    pw = "1" * 11
    res = compute_strength(pw)
    print(res)
    assert compute_strength(pw)[0] == 1

def test_password_with_length_5_gives_0_point():
    pw = "1" * 5
    assert compute_strength(pw)[0] == 0

def test_password_empty_gives_0_point():
    pw = ""
    assert compute_strength(pw)[0] == 0

def test_password_with_number_and_letter_gives_1_point():
    pw = "1a"
    assert compute_strength(pw)[0] == 1

def test_password_with_special_characters_gives_1_point():
    pw = "#%&+_-"
    assert compute_strength(pw)[0] == 1

def test_password_with_bad_chars_0_point():
    pw = "!"
    assert compute_strength(pw)[0] == 0

def test_password_with_length_11_and_numbers_letters_and_specialchars_gives_3_point():
    pw = "a1&mdlasnam"
    assert compute_strength(pw)[0] == 3

def test_password_with_length_3_and_numbers_letters_and_specialchars_gives_2_point():
    pw = "a1&"
    assert compute_strength(pw)[0] == 2

def test_password_with_length_11_and_numbers_letters_2_point():
    pw = "a1" * 11
    assert compute_strength(pw)[0] == 2

def test_password_with_length_22_and_specialchars_2_point():
    pw = "a&" * 11
    assert compute_strength(pw)[0] == 2
