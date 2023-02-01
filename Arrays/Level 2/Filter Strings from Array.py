##Problem Statement: Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
##Problem Link: https://edabit.com/challenge/EfEpbcGjXQYDFcdxF

#Examples:
#filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
#filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
#filter_list(["Nothing", "here"]) ➞ []

#Solution:
def filter_list(l):

    #Return list elements of integers only
    return [element for element in l if type(element) == int]
