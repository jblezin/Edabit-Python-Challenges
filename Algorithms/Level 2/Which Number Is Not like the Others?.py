##Problem Statement: Create a function that takes a list of numbers and returns the number that's unique.
##Problem Link: https://edabit.com/challenge/GaXXfmpM72yCHag9T

#Examples
#unique([3, 3, 3, 7, 3, 3]) ➞ 7
#unique([0, 0, 0.77, 0, 0]) ➞ 0.77
#unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0

#Solution:
def unique(list):

    #Count occurrences of each element in list & return element
    return sum(element for element in list if list.count(element) == 1)
