# Task
#
# Premutation – please see a simple definition of premutation here:
# http://www.amathsdictionaryforkids.com/qr/p/permutations.html
#
#
# We  need  to  write  a  function  that  accepts  an  array
# of  unique  integers  and  returns  an  array  of  ALL
# permutations of those integers. No particular order.
#
# NB: if the input array is empty, then your function should return an empty array
# NB:  we  are  looking  for  permutations  without  repetition.
#
# For  example:    [1,1,2]  or  [3,2,3]  are  not allowed

def array_is_unique(array):
    if len(set(array)) < len(array):
        return False
    else:
        return True


def array_is_filled(array):
    if not array:
        print(f' your array is empty')
    return False

permeutations = []
array = input('Please enter an array of unique integers separated by a comma!').split(',')

if array_is_unique(array) and array_is_filled(array):
    permeutations












