##Problem Statement: Create a function that returns the minimum number of elements removed to make the sum of all elements in a list even.
##Problem Link: https://edabit.com/challenge/sGrSbcXGeMGEc3HXR

#Examples:
#minimum_removals([1, 2, 3, 4, 5]) ➞ 1
#minimum_removals([5, 7, 9, 11]) ➞ 0
#minimum_removals([5, 7, 9, 12]) ➞ 1

#Solution:
def minimum_removals(lst):

    #Return if an element should be removed
    return  (0 if sum(lst) % 2 == 0 else 1)
