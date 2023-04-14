# 1.1 What does SDLC stand for? 
SDLC stands for Software Development Life Cycle. It is a structured process where software development teams design, develop, and maintain software: dividing the production cycle into stages.

# 1.2   What exception is thrown when you divide a number by 0?	1 mark
DivideByZeroException


# 1.3   What is the git command that moves code from the local repository to the remote repository? 	1 mark
Git Push

# 1.4   What does NULL represent in a database? 	   
The absence of a value in a a database

# 1.5   Name 2 responsibilities of the Scrum Master 
1. Scrum Masters facilitate the collaborative review and discussion revolving around the development process of a project: 

2. Scrum Masters that there is transparency between team and the scrum king: people collaborate 


# 1.6   Name 2 debugging methods, and when you would use them.	  4 marks
1. The user can use a series of print statement after lines of code in order to show the output of the code at different points, which can be used ot determine the point at which the code is encountering a problem. For example, if there is a logical error
2. The suer can be used the IDE's in-built debugger tool which parses the cod eline by line to identify the potential errors in the code, set breakpoints to pause execution at points which aids in solving complex bugs.

# 1.7   Looking at the following code, describe a case where this function
           would throw an error when called. Describe this case and talk about
           what exception handling you’ll need. 

If either ‘price’ or ‘cash given’ had a non-numeric data type (ie. were a string). 

To solve this, a try-except block using the float() function to convert the arguments to floats, to be caught with a ValueError exception. 
def can_pay(price, cash_given):
   if cash_given >= price:
       return True
   else:
       return False

def can_pay(price, cash_given):
   try:
       price = float(price)
       cash_given = float(cash_given)
   except ValueError:
       print("Error: price and cash_given must be numeric values")
       return False

   if cash_given >= price:
       return True
   else:
       return False


# 1.8    What is git branching? Explain how it is used in Git.
A feature of Git which allows software developers to create independent lines of development from the main code, creating a copy of the codebase at a specific point in time which do not affect the master copy of code in the main branch. changes to it can be made independently to be merged back into the main branch if desired. This is used by developers to  work on certain features in isolation, conduct bug fixes, without interfering with the work of others


# 1.9  Design a restaurant ordering system. 
### You do not need to write code, but describe a high-level approach: 
a.	Draw a list of key requirements
-	A userfriendly interface which make sit easy fir customers to navigate, select and place orders. It must be intuitive
-	Integration with a payment system, allowing the user to pay for their items
-	Customisable menu, where users cann add or remove ingredients from their order
-	Integration with the restaurant’s stock database, making sure it removes items off the menu when they run out

b.	What are your main considerations and problems?
-	Security concerns, considering individuals payment information is being transmitted. It should also be generally robust, fending against fraudulent or malicious activity.
-	The scalability of the system, being designed to handle the traffic of a  large volume of users at the same time
-	Integration with other software and data, such as online banking and databases
c.	What components or tools would you potentially use? 
-	Front-end development tools such as React to build the user interface. 
-	Backend development tools such as Node.js, Ruby on Rails, or Django for building server-side logic.
-	Payment integration tools such as Stripe or PayPal for handling payment transactions.
-	Cloud services such as AWS or Azure for the storage of data and scalability of the software


