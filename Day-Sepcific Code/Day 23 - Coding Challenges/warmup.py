"""
TASK 1 (copy-paste this task in the dialog window to share with the student)
Write a function that accepts a string and returns a string where all
characters of the original string are now in alphabetical order. For example,
"Code" --> "Cdeo"
"""


# EXAMPLE SOLUTION

def convert_to_abc_chars(string):
    s = "".join(sorted(string))
    return s





print(convert_to_abc_chars("Code"))
print(convert_to_abc_chars("CodeFirstGirls"))



"""
TASK 2 (copy-paste this task in the dialog window to share with the student)
Accept a string and use list comprehension to generate as many strings 'CFG' 
in an array as many letters are in the given string. For example:
string = "Code" (4 letters in the string) --> ["CFG", "CFG", "CFG", "CFG"] 
NB: it is entirely up to you whether to write function or just write script
in the console.
"""
# EXAMPLE SOLUTION


def array_generator(given_string, default_string='CFG'):
    res = [ default_string for i in range(len(given_string)) ]
    return res




print(array_generator("Code"))