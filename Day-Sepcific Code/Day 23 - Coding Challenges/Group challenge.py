"""
Ways to Change a Banknote -- SOLUTION
"""

banknote = int(input('Enter the amount of money you have'))
denoms =


def num_ways(note, denoms):
   ways = [0 for amount in range(note + 1)] # if we had 10, this makes an array of 0 to 11
   ways[0] = 1

   for denom in denoms: # [1,5,10, 25]
      for amount in range(1, note+1): # fo
         if denom <= amount:
            ways[amount] = ways[amount] + ways[amount-denom]
      return ways[note]

