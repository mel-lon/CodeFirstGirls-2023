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