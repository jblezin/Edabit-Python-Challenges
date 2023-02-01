##Problem Statement: Create a function to find None in a list of numbers. The return value should be the index where None is found. If None is not found in the list, then return -1.
##Problem Link: https://edabit.com/challenge/xPB3jeeNRLqRQ3Dwe

#Examples:
#find_none([1, 2, None]) ➞ 2
#find_none([None, 1, 2, 3, 4]) ➞ 0
#find_none([0, 1, 2, 3, 4]) ➞ -1

#Solution:
def find_none(lst):

    #Return index of 'None' or -1
    return lst.index(None) if None in lst  else -1
