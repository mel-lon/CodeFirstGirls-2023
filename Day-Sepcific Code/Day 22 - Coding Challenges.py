"""
TASK 1

Use the string "CodeFirstGirls" and only take a part of it: "Girls". The turn
the word "Girls" into "G-i-r-l-s".

NB: it is entirely up to you whether to write function or just write script
in the console.
"""

# EXAMPLE SOLUTION

string = "CodeFirstGirls"
word = string[-5:]
chars = list(word)
print('-'.join(chars))



#
#
#
# # word = string[9:]
# word = string[-5:]
# chars = list(word)
# result = "-".join(chars)
# print(result)
#
#
# ############################################################
#
#
# """
# TASK 2
#
# Spice Girls ("Wannabe")
#
# '''
lyrics = ("Yo, I'll tell you what I want, what I really, really want So tell me what you want, what you really, really want I'll tell you what I want, what I really, really want So tell me what you want, what you really, really want I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna really, really, really wanna zigazig ah").split()
print(lyrics)
count = 0
for word in lyrics:
    if word == 'really':
        count += 1
    elif word == 'really,':
        count+=1

print(f'These lyrics say really {count} times')





'''
#
#Count how many times the word "really" appears in the Spice Girls lyrics.
#
# NB: it is entirely up to you whether to write function or just write script
# in the console.
# """







# # EXAMPLE SOLUTION
# # (just a quick solution that doesn't handle special cases)
#
lyrics = 
"Yo, I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna, (ha)
I wanna really, really, really wanna zigazig ah"

words = lyrics.split(' ')
words = [word.strip(',') for word in words]
result = words.count('really')
print(result)