# Question 1
def processing_queue(input_file):
    queue = []
    with open(input_file, 'r') as file:
        for line in file:
            command, name = line.strip().split(' ')
            if command == "JUMP":
                queue.insert(0, name)
            elif command == "JOIN":
                queue.append(name)

    return queue


# Part B

# The time complexity of the solution is O(n), where n represents the number of commands in
# the input file. This is because the program iterates through each line of the file to process
# the commands, resulting in a time complexity directly proportional to the number of lines,
# which is equivalent to the number of commands in this case.
#
# The solution has a space complexity of O(n), where n denotes the number of commands in the input file.
# This is due to the program storing the names of people in a list.
# As the number of commands increases, the size of the list grows linearly, resulting in a
# space requirement that is directly proportional to the number of commands in the input file.
#
# Assumptions:
#
# Firstly, the solution assumes that the input file is not excessively large and
# can be comfortably loaded into memory. If the input file is extremely large,
# it may require a different approach, such asreading the file line by line instead of
# loading the entire content into memory at once
#
# Secondly, the solution assumes the input file is correctly formatted, with each
# line containing a command and a name separated by a space. The program assumes
# that the format is consistent and adheres to the expected structure.
#
# Thirdly,  The solution assumes that the commands in the input file should be processed
# sequentially, in the order they appear. There is no parallel or concurrent execution of
# commands considered in this solution.
#
# Finally, The program assumes that the commands in the input file are either "JUMP" or "JOIN"
# and that the names provided are valid. It does not perform explicit validation on the commands
# or names.


# Question 2

def find_nth_number(n):
    if n == 1:
        return 8
    else:
        return find_nth_number(n - 1) + 7


#
# Question 3

base_url = "https://codefirstgirls.com/"
current_url = base_url

while True:
    print("You are currently on the URL", current_url)
    print("Where are you clicking?")

    if current_url == base_url:
        print("Options: Courses, Opportunities")
        choice = input()
        if choice.lower() == "courses":
            current_url += "courses"
        elif choice.lower() == "opportunities":
            current_url += "opportunities"

    elif current_url == base_url + "courses":
        print("Options: CFGDegree, Back")
        choice = input()
        if choice.lower() == "cfgdegree":
            current_url += "/cfgdegree"
        elif choice.lower() == "back":
            current_url = base_url

    elif current_url == base_url + "opportunities":
        print("Options: Ambassadors, Back")
        choice = input()
        if choice.lower() == "ambassadors":
            current_url += "/ambassadors"
        elif choice.lower() == "back":
            current_url = base_url

    elif current_url == base_url + "courses/cfgdegree":
        print("Options: Back")
        choice = input()
        if choice.lower() == "back":
            current_url = base_url + "courses"

    elif current_url == base_url + "opportunities/ambassadors":
        print("Options: Back")
        choice = input()
        if choice.lower() == "back":
            current_url = base_url + "opportunities"

    print()


# Question 3b

# The time complexity of the solution can be considered as O(1) since the number of URLs and user
# choices does not have a significant impact on the number of iterations or operations performed by
# the program. The number of URLs is fixed, and the user choices only affect the navigation path within
# the predetermined URLs.
#
# The space complexity of the solution is also O(1) since the amount of memory used by the program
# remains constant regardless of the number of URLs or user choices. The program only stores the base
# URL and the current URL, and it does not require additional data structures or memory allocation that grows with the input size.
#
# Assumptions:
#
# Firstly, the provided URLs are the only valid URLs in the simulation. Other URLs or variations are not
# considered.
#
# Secondly, the user's input is assumed to be valid and matches the available options exactly. ' \'No input validation or error handling is implemented.
#
# Thirdly, the simulation loop runs indefinitely until an external force or condition breaks the loop.
#
# Fourthly, the program does not handle cases where the user navigates to an invalid or non-existent URL.
# Error handling and validation are not included in the code.
#
# Finally, the program focuses on simulating the navigation and printing the current URL after each move,
# rather than implementing full website functionality or page rendering.