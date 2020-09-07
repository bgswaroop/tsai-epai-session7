# EPAi session7 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session7 objectives
This assignment, helps to code the concepts that are learnt in the session 7 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

---

The test cases can be executed by executing _pytest_, from python shell
 - Map, Filter & Zip
 - Reducing Functions
 - Partial Functions
 - The Operator Module
 
---

### Functions



**q1_is_fibonacci(number :  int) -> bool**

    Task :  Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not.
    You can use a pre-calculated list/dict to store fib numbers till 10000
     : param number :  An integer value to test if an input is fibonacci
     : return :  Bool value, indicating the result of the test

**q21_add_iterables(a :  list, b :  list) -> int**

    Task 2.1 :  add 2 iterables a and b such that a is even and b is odd
     : param a :  list of integers
     : param b :  list of integers
     : return :  an integer, indicating the sum

**q22_strip_vowels(input_string :  str)**

    Task 2.2 :  strips every vowel from a string provided (tsai>>t s)
     : param input_string :  any input string
     : return :  string without vowels

**q23_relu(array :  list) -> list**

    Task 2.3 :  acts like a ReLU function for a 1D array
     : param array :  list of integers
     : return :  list of integers after transforming with ReLU

**q24_sigmoid(array :  list) -> list**

    Task 2.4 :  acts like a Sigmoid function for a 1D array
     : param array :  list of integers
     : return :  list of integers after transforming with Sigmoid

**q25_shift_characters_by_5(input_string :  str) -> str**

    Task 2.5 :  takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
     : param input_string :  any string of lower case alphabets
     : return :  string rotated by 5 places

**q3_check_swear_words(paragraph :  str) -> bool**

    Task 3 :  A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the
    swear words mentioned in https : //github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
     : param paragraph :  a string with some words
     : return :  True if the paragraph contains any swear words

**q41_add_evens(array :  list) -> int**

    Task 4.1 :  Using reduce function add only even numbers in a list
     : param array :  list of integers
     : return :  integer (sum of evens)

**q42_find_biggest_printable_ascii_char(input_string :  str) -> int**

    Task 4.2 :  Using reduce function find the biggest character in a string (printable ascii characters)
    ord in the range 32-127
     : param input_string :  string
     : return :  integer - ord of the largest ascii character, return 0 if no printable ascii character

**q43_add_3rd_element(array :  list) -> int**

    Task 4.3 :  Using reduce function adds every 3rd number in a list
     : param array :  list of integers
     : return :  integer (sum of every 3rd number in a list)

**q5_generate_random_number_plates() -> list**

    Task 5 :  Using randint, random.choice and list comprehensions, write an expression that generates 15 random
    KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets.
    10<<DD<<99 & 1000<<DDDD<<9999
     : return :  list of strings, where each string represents a number plate

**q61_generate_random_number_plates(state :  str, num_range :  tuple) -> list**

    Task 6.1 :  Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided.
     : param state :  two capital letters
     : param num_range :  any integer x, such that 0 <= x <= 9999
     : return :  list of strings, where each string represents a number plate


---

### Unit tests

**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_q1_is_fibonacci()**

    Testing the method q1_is_fibonacci
     : return :  None

**test_q21_add_iterables()**

    Testing the method q21_add_iterables
     : return :  None

**test_q22_strip_vowels()**

    Testing the method strip_vowels
     : return :  None

**test_q23_relu()**

    Testing the method relu
     : return :  None

**test_q24_sigmoid()**

    Testing the method sigmoid
     : return :  None

**test_q25_shift_characters_by_5()**

    Testing the q25_shift_characters_by_5 method
     : return :  None

**test_q3_check_swear_words()**

    Testing the check_swear_words method
     : return :  none

**test_q41_add_evens()**

    Testing the method q41_add_evens
     : return :  None

**test_q42_find_biggest_printable_ascii_char()**

    Testing the method q42_find_biggest_printable_ascii_char
     : return :  None

**test_q43_add_3rd_element()**

    Testing the method q43_add_3rd_element
     : return :  None

**test_q5_generate_random_number_plates()**

    Testing the method q5_generate_random_number_plates
     : return :  None

**test_q61_generate_random_number_plates()**

    Testing the method q61_generate_random_number_plates
     : return :  None

**test_q62_generate_random_number_plates_using_partial()**

    Testing the method q62_generate_random_number_plates_using_partial
     : return :  None

---

#### 