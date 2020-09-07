import inspect
import os
import re
import string

import session7
from session7 import *


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_q1_is_fibonacci():
    """
    Testing the method q1_is_fibonacci
    :return: None
    """
    result = q1_is_fibonacci(7)
    assert result is False

    result = q1_is_fibonacci(-7)
    assert result is False

    result = q1_is_fibonacci(24157817)
    assert result is True


def test_q21_add_iterables():
    """
    Testing the method q21_add_iterables
    :return: None
    """
    a = list(range(1, 11, 1))
    b = list(range(10, 101, 10))

    result = q21_add_iterables(a, b)
    assert result == 0


def test_q22_strip_vowels():
    """
    Testing the method strip_vowels
    :return: None
    """

    result = q22_strip_vowels('tsai')
    assert result == 'ts'


def test_q23_relu():
    """
    Testing the method relu
    :return: None
    """

    result = q23_relu([1, -1, 0])
    assert result == [1, 0, 0]


def test_q24_sigmoid():
    """
    Testing the method sigmoid
    :return: None
    """

    result = q24_sigmoid([1, -1, 0])
    assert result == [0.7310585786300049, 0.2689414213699951, 0.5]


def test_q25_shift_characters_by_5():
    """
    Testing the q25_shift_characters_by_5 method
    :return: None
    """
    result = q25_shift_characters_by_5('tsai')
    assert result == 'yxfn'


def test_q3_check_swear_words():
    """
    Testing the check_swear_words method
    :return: none
    """
    result = q3_check_swear_words('She accidentally stepped on a poop')
    assert result is True

    result = q3_check_swear_words('Sai Ram')
    assert result is False


def test_q41_add_evens():
    """
    Testing the method q41_add_evens
    :return: None
    """
    result = q41_add_evens([1, 2, 3, 4, 5])
    assert result == 6

    result = q41_add_evens([1, 3, 5])
    assert result == 0


def test_q42_find_biggest_printable_ascii_char():
    """
    Testing the method q42_find_biggest_printable_ascii_char
    :return: None
    """

    result = q42_find_biggest_printable_ascii_char('Sai')
    assert result == ord('i')


def test_q43_add_3rd_element():
    """
    Testing the method q43_add_3rd_element
    :return: None
    """
    result = q43_add_3rd_element([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert result == 12


def test_q5_generate_random_number_plates():
    """
    Testing the method q5_generate_random_number_plates
    :return: None
    """
    result = q5_generate_random_number_plates()
    assert len(result) == 15
    for x in result:
        assert len(x) == 10
        assert x[0:2] == 'KA'
        assert x[2: 4].isdigit and 10 <= int(x[2: 4]) <= 99
        assert x[4] in string.ascii_uppercase and x[5] in string.ascii_uppercase
        assert x[6:].isdigit and 1000 <= int(x[6:]) <= 9999


def test_q61_generate_random_number_plates():
    """
    Testing the method q61_generate_random_number_plates
    :return: None
    """
    state = 'DL'
    min_num_plate = 2345
    max_num_plate = 7854
    result = q61_generate_random_number_plates(state=state, num_range=(min_num_plate, max_num_plate))
    assert len(result) == 15
    for x in result:
        assert len(x) == 10
        assert x[0:2] == state
        assert x[2: 4].isdigit and 10 <= int(x[2: 4]) <= 99
        assert x[4] in string.ascii_uppercase and x[5] in string.ascii_uppercase
        assert x[6:].isdigit and min_num_plate <= int(x[6:]) <= max_num_plate


def test_q62_generate_random_number_plates_using_partial():
    """
    Testing the method q62_generate_random_number_plates_using_partial
    :return: None
    """
    state = 'DL'
    result = q62_generate_random_number_plates_using_partial(state=state)
    assert len(result) == 15
    for x in result:
        assert len(x) == 10
        assert x[0:2] == state
        assert x[2: 4].isdigit and 10 <= int(x[2: 4]) <= 99
        assert x[4] in string.ascii_uppercase and x[5] in string.ascii_uppercase
        assert x[6:].isdigit and 1000 <= int(x[6:]) <= 9999
