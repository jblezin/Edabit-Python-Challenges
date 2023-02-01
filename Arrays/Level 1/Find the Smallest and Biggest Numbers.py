##Problem Statement: Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).
##Problem Link: https://edabit.com/challenge/y9Rans4Ry5oW74cat

#Examples:
#min_max([1, 2, 3, 4, 5]) ➞ [1, 5]
#min_max([2334454, 5]) ➞ [5, 2334454]
#min_max([1]) ➞ [1, 1]

#Solution:
def min_max(numbers):

    #Return largest & smallest number from list
    return [min(numbers),max(numbers)]
