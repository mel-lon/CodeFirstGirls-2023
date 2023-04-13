"""
Palindrome Substring Challenge -- SOLUTION
Please watch the demo video, which explains how to approach and solve
this challenge.
This is one of the multiple possible solutions (there might be many others)
This one is:
O(n^3) time | O(n) space
"""

# EXAMPLE SOLUTION


def is_palindrome(string):
    """
    Check if a string is a palindrome
    :param string: any string
    :return: boolean
    """
    left_idx = 0
    right_idx = len(string) - 1  # because idx start with 0, but len isn't 0 1 2 3 4 5 6 7 8
    while left_idx < right_idx:

        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def palindrome_substring(string):
    current_longest = ""

    # these 3 lines give you all possible substrings in the string
    # you can even run these lines in a console to see how it works
    for num1 in range(len(string)):
        for num2 in range(num1, len(string)):
            substring = string[num1: num2 + 1]

            if len(substring) > len(current_longest) and \
                    is_palindrome(substring):
                current_longest = substring
    return current_longest

####################### 1 hr 10 for explanation of this one