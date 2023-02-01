##Problem Statement: Given an unsorted list, create a function that returns the nth smallest integer (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).
##Problem Link: https://edabit.com/challenge/TApvBKg2WiAXPnwLS

#Examples:
#nth_smallest([1, 3, 5, 7], 1) ➞ 1
#nth_smallest([1, 3, 5, 7], 3) ➞ 5
#nth_smallest([1, 3, 5, 7], 5) ➞ None
#nth_smallest([7, 3, 5, 1], 2) ➞ 3

#Solution:
def nth_smallest(lst, smallest):

    #Return the smallest number
    return (None if smallest > len(lst) else sorted(lst)[smallest -1])
