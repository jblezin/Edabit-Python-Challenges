##Problem Statement: Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
##Problem Link: https://edabit.com/challenge/nunJurLEibCyn8fzn

#Examples:
#filter_list([1, 2, "a", "b"]) ➞ [1, 2]
#filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
#filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]

#Solution:
def filter_list(lst):

    #Return list with integers only
    return [element for element in lst if type(element) == int]
