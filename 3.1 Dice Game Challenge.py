# Question 6
# Write a program that simulates rolling two dice together 100 times.

import random


outcomes = []
for x in range(100):
    roll1 = random.randint(1,6)
    outcomes.append(roll1)
    roll2 = random.randint(1,6)
    outcomes.append(roll2)

print(outcomes)



# Record the results of each roll to know how many 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, 11s and 12s were rolled.
stats = {}
for i in outcomes:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

print(stats)



# From this work out the probability of getting each number.

frequencies = {key: float(value) / sum(stats.values()) for (key, value) in stats.items()}
print(frequencies)

# Tell the user they have two dice
search = int(input("You have two dice to roll, what is the number you're looking for?"))
print(f"having rolled two dice 100 times, the probability of rolling the value {search} is {frequencies.get(search)}")
# and ask them what number they are trying to get,
# then return the probability of them getting that number.
#
#
