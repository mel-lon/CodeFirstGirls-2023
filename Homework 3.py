# #Question 1
#     #Create a program that tells you whether or not you need sunglasses when you leave the house.
#     #The program should:
#     #1. Ask you if it is sunny using input()
#     #2. If the input is 'y', it should output 'Take your sunglasses’
#     #3. If the input is 'n', it should output 'You don't need sunglasses’
#
# status = str(input("Is it funny outside? type 'y'/'n'"))
# if status == 'y':
#     print('Take your sunglasses')
# elif status =='n':
#     print("You don't need sunglasses")
# else:
#     print('enter a valid response')
#
#
#
# #Question 2
#     #I want to hire a venue for my birthday for 3 hours. The venue hire costs £200 per hour and a refundable 10% deposit. I've written a program to check that I can afford the cost, but something doesn't seem right.
#     #Have a look at my program and work out what I've done wrong:
# my_money = int(input('How much money do you have? '))
# hour = 3
# venue_cost = (200*hour) + 1.1 #change this to (200*1.1*hours)
# if my_money < venue_cost:
#   print('You can afford the venue')
# else :
#   print('You cannot afford the venue')
#
#
#
# # Question 3
# #You work as a primary school teacher and are teaching numbers by showing how they are
# #composed of units of ten and one.
# #Write a program for students to play with to understand this concept.
#
#
#   #You will be asking for them to enter numbers between 1 and 25
#   #(they haven’t gone higher than that!),
#   #so you do not need to consider bigger numbers.
#   #The function needs to print to the screen
#   #and the message must be grammatically correct
#   #and in the format shown below.
#
#
#
# #pip install num2words
# from num2words import num2words
#
# def unit_breakdown(number):
#     tens = number % 10
#     units = number - (number%10)
#     if units > 1:
#         print(f"{num2words(tens).capitalize()} Tens, {num2words(units).capitalize()} Ones")
#     else:
#         print(f"{num2words(tens).capitalize()} Tens, One Ones")
#
#
# number = int(input("Enter a number between 1 an 25"))
#
# if (number) <= 25:
#     unit_breakdown(number)
# else:
#     print('Please enter a valid number')
#
#
#Question 4
students = ['Chloe', 'Anna', 'Lauren', 'Shreya', 'Siobhan']
print(sorted(students))


#Question 5
# You are trying to get rid of your old stuff in a bootsale and want to set
# up a program to quickly return the price when given an item.
# ●	Create a ‘shop’ dictionary with at least 4 items and respective prices.
# ●	Write some code that will take in the name of an item and output the price

# shop = [
# {'item': 'trainers', 'price': 70},
# {'item': 'painting', 'price': 100},
# {'item': 'Shirt', 'price': 60},
# {'item': 'ipod', 'price': 80}]
#
#
# check = str(input('What is being looked for?'))
#
#
# for x in shop:
#     if x['name'] == check:
#         print(x['price'])
#

# # Question 6
# # Write a program that simulates rolling two dice together 100 times.
#
# import random
#
#
# outcomes = []
# for x in range(100):
#     roll1 = random.randint(1,6)
#     outcomes.append(roll1)
#     roll2 = random.randint(1,6)
#     outcomes.append(roll2)
#
# print(outcomes)
#
#
#
# # Record the results of each roll to know how many 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, 11s and 12s were rolled.
# stats = {}
# for i in outcomes:
#     if i in stats:
#         stats[i] += 1
#     else:
#         stats[i] = 1
#
# print(stats)
#
#
#
# # From this work out the probability of getting each number.
#
# frequencies = {key: float(value) / sum(stats.values()) for (key, value) in stats.items()}
# print(frequencies)
#
# # Tell the user they have two dice
# search = int(input("You have two dice to roll, what is the number you're looking for?"))
# print(f"having rolled two dice 100 times, the probability of rolling the value {search} is {frequencies.get(search)}")
# # and ask them what number they are trying to get,
# # then return the probability of them getting that number.
#

