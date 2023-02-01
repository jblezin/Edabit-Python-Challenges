##Problem Statement: Create a function that takes a list and returns the difference between the biggest and smallest numbers.
##Problem Link: https://edabit.com/challenge/XsJLwhAddzbxdQqr4

#Examples:
#difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32.

#difference_max_min([44, 32, 86, 19]) ➞ 67
# Smallest number is 19, biggest is 86.

#Solution:
def difference_max_min(list):

    #Return difference between smallest & largest numbers in list
    return abs(min(list) - max(list))
