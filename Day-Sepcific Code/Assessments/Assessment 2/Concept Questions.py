#    Write a function that takes in an input and checks to see if it’s an
#              isogram.
#    The function should return True or False.
#
#              An isogram is a word where no letter is repeated.
#              Examples include:
# ●"isogram"
# ●"uncopyrightable"
# ●“ambidextrously


word = input('Please enter a word to be checked').lower()

def isogram_checker(word):
    letters = []
    for letter in word:
        if letter.isalpha():
            if letter in letters:
                return False
            else:
                letters.append(letter)
    return True

print(isogram_checker(word))




# Make a new test file and write comprehensive   unit tests for the
#              function you wrote in 2.1
#              For each test case add a comment stating why you chose that case.
#########See next file