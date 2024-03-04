"""
Lab 6 - Strings and Tuples 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  Ata
Due Date: This Friday (Mar. 1) 11am.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    reversed_string = ''  # Initialize an empty string to store the reversed string
    for i in range(len(s)-1, -1, -1):  # Iterate through the string in reverse order
        char = s[i]
        reversed_string += char  # Append each character to the reversed string
    return reversed_string
    

assert reverse_str('app') == "ppa"
assert reverse_str("COMP115") == "511PMOC"
assert reverse_str("Abd") == "dbA"



"""
Exercise 2 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    s = s.lower()
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for char in s:
        if char in vowels:
            count = count + 1
    return count
    
assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0
assert count_vowels("BANANA") == 3




"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: We have implemented a function removing duplicates for a list in week 6. Similar.
"""
def remove_duplicates(s):
    """
    This function removes duplicates from string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"

    Parameters:
    - s (string): String in which duplicates will be removed.

    Returns:
    - (string): String without duplicates.

    """
    duplicate_free = ''
    for char in s:
        if char not in duplicate_free:
            duplicate_free += char
    return duplicate_free

assert remove_duplicates("apple") == "aple"
assert remove_duplicates("orange") == "orange"
assert remove_duplicates("school") == "schol"



"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    This function returns first index of character t in a string s.

    E.g.,
    >>> find_index("Abd", 'b') 
    1

    Parameters:
    - s (string): String where we're looking for character t.
    - t (string): Character we're looking for in the string s.

    Returns:
    - (int): Index of character t.

    """
    index = -1
    for i in range(len(s)):
        if s[i] == t:
            index = i
            break
    return index

assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    This function returns project completion day.
    
    E.g.,
    >>> project_completion_day('Monday', 4)
    'Friday'

    Parameters:
    - day (string): Current day.
    - days_to_completion (int): Days to completion.

    Returns:
    - (string): Project completion day.

    """
    index = days_week.index(day) + days_to_completion
    if index > 6:
        index %= 7
    return days_week[index]

assert project_completion_day('Tuesday', 5) == 'Sunday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Monday', 21) == 'Monday'

"""
Congratulations on finishing your lab6. Hope you feel more confident on function implementation.

Now you just need to upload it to your GitHub repository. That's all.
"""