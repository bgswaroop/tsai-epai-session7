import math
import random
from functools import reduce, partial


def q1_is_fibonacci(number: int) -> bool:
    """
    Task: Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not.
    You can use a pre-calculated list/dict to store fib numbers till 10000
    :param number: An integer value to test if an input is fibonacci
    :return: Bool value, indicating the result of the test
    """

    # Generating a pre-calculated fibonacci sequence with upto 10000 numbers
    fib = [1, 1]
    for _ in range(10000):
        fib.append(fib[-1] + fib[-2])

    # Check if the number belongs to the fib list
    result = any(filter(lambda x: number == x, fib))

    return result


def q21_add_iterables(a: list, b: list) -> int:
    """
    Task 2.1: add 2 iterables a and b such that a is even and b is odd
    :param a: list of integers
    :param b: list of integers
    :return: an integer, indicating the sum
    """
    result = reduce(lambda x, y: x + y, [x[0] + x[1] for x in zip(a, b) if x[0] % 2 == 0 and x[1] % 2 == 1], 0)
    return result


def q22_strip_vowels(input_string: str):
    """
    Task 2.2: strips every vowel from a string provided (tsai>>t s)
    :param input_string: any input string
    :return: string without vowels
    """
    result = ''.join([x for x in input_string if x not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}])
    return result


def q23_relu(array: list) -> list:
    """
    Task 2.3: acts like a ReLU function for a 1D array
    :param array: list of integers
    :return: list of integers after transforming with ReLU
    """

    result = list(map(lambda x: x if x >= 0 else 0, array))
    return result


def q24_sigmoid(array: list) -> list:
    """
    Task 2.4: acts like a Sigmoid function for a 1D array
    :param array: list of integers
    :return: list of integers after transforming with Sigmoid
    """

    result = list(map(lambda x: math.exp(x) / (math.exp(x) + 1), array))
    return result


def q25_shift_characters_by_5(input_string: str) -> str:
    """
    Task 2.5: takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
    :param input_string: any string of lower case alphabets
    :return: string rotated by 5 places
    """
    result = ''.join([chr((ord(x) - ord('a') + 5) % 26 + ord('a')) for x in input_string])
    return result


def q3_check_swear_words(paragraph: str) -> bool:
    """
    Task 3: A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the
    swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
    :param paragraph: a string with some words
    :return: True if the paragraph contains any swear words
    """

    import urllib.request
    content = urllib.request.urlopen(
        'https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt')
    swear_words = content.read().decode('utf-8').split('\n')
    paragraph_words = paragraph.split(' ')

    # Check if words in paragraph_words belongs to the swear_words
    result = any([any(filter(lambda x: word == x, swear_words)) for word in paragraph_words])
    return result


def q41_add_evens(array: list) -> int:
    """
    Task 4.1: Using reduce function add only even numbers in a list
    :param array: list of integers
    :return: integer (sum of evens)
    """
    result = reduce(lambda x, y: x if y % 2 == 1 else x + y, array, 0)
    return result


def q42_find_biggest_printable_ascii_char(input_string: str) -> int:
    """
    Task 4.2: Using reduce function find the biggest character in a string (printable ascii characters)
    ord in the range 32-127
    :param input_string: string
    :return: integer - ord of the largest ascii character, return 0 if no printable ascii character
    """
    result = reduce(lambda x, y: ord(y) if 32 <= ord(y) <= 127 and ord(y) > x else x, input_string, 0)
    return result


def q43_add_3rd_element(array: list) -> int:
    """
    Task 4.3: Using reduce function adds every 3rd number in a list
    :param array: list of integers
    :return: integer (sum of every 3rd number in a list)
    """

    result = reduce(lambda x, y: x if y[0] % 3 != 0 else (0, x[1] + y[1]), enumerate(array), (0, 0))[1]
    return result


def q5_generate_random_number_plates() -> list:
    """
    Task 5: Using randint, random.choice and list comprehensions, write an expression that generates 15 random
    KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets.
    10<<DD<<99 & 1000<<DDDD<<9999
    :return: list of strings, where each string represents a number plate
    """
    result = ['KA' + str(random.randint(10, 99)) + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) +
              str(random.randint(1000, 9999)) for _ in range(15)]
    return result


def q61_generate_random_number_plates(state: str, num_range: tuple) -> list:
    """
    Task 6.1: Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided.
    :param state: two capital letters
    :param num_range: any integer x, such that 0 <= x <= 9999
    :return: list of strings, where each string represents a number plate
    """

    assert 1000 <= num_range[0] <= num_range[1] <= 9999

    result = [state + str(random.randint(10, 99)) + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) +
              str(random.randint(num_range[0], num_range[1])) for _ in range(15)]
    return result


q62_generate_random_number_plates_using_partial = partial(q61_generate_random_number_plates, num_range=(1000, 9999))
