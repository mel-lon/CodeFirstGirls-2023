#Question 1
    #Create a program that tells you whether or not you need sunglasses when you leave the house.
    #The program should:
    #1. Ask you if it is sunny using input()
    #2. If the input is 'y', it should output 'Take your sunglasses’
    #3. If the input is 'n', it should output 'You don't need sunglasses’

status = str(input("Is it funny outside? type 'y'/'n'"))
if status == 'y':
    print('Take your sunglasses')
elif status =='n':
    print("You don't need sunglasses")
else:
    print('enter a valid response')



#Question 2
    #I want to hire a venue for my birthday for 3 hours. The venue hire costs £200 per hour and a refundable 10% deposit. I've written a program to check that I can afford the cost, but something doesn't seem right.
    #Have a look at my program and work out what I've done wrong:
my_money = int(input('How much money do you have? '))
hour = 3
venue_cost = (200*hour) + 1.1 #change this to (200*1.1*hours)
if my_money < venue_cost:
  print('You can afford the venue')
else :
  print('You cannot afford the venue')



# Question 3
#You work as a primary school teacher and are teaching numbers by showing how they are
#composed of units of ten and one.
#Write a program for students to play with to understand this concept.


  #You will be asking for them to enter numbers between 1 and 25
  #(they haven’t gone higher than that!),
  #so you do not need to consider bigger numbers.
  #The function needs to print to the screen
  #and the message must be grammatically correct
  #and in the format shown below.



#pip install num2words
from num2words import num2words

def unit_breakdown(number):
    tens = number % 10
    units = number - (number%10)
    if units > 1:
        print(f"{num2words(tens).capitalize()} Tens, {num2words(units).capitalize()} Ones")
    else:
        print(f"{num2words(tens).capitalize()} Tens, One Ones")


number = int(input("Enter a number between 1 an 25"))

if (number) <= 25:
    unit_breakdown(number)
else:
    print('Please enter a valid number')
