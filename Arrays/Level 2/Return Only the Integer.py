##Problem Statement: Write a function that takes a list of elements and returns only the integers.
##Problem Link: https://edabit.com/challenge/DG2HLRqxFXxbaEDX4

#Examples:
#return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
#return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]
#return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]
#return_only_integer(["String",  True,  3.3,  1]) ➞ [1]

#Solution:
def return_only_integer(lst):

    #Return list of integers only
    return list(filter(lambda element:type(element) == int, lst))
