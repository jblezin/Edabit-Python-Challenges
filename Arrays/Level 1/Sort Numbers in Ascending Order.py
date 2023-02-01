##Problem Statement: Create a function that takes a list of numbers and returns a new list, sorted in ascending order (smallest to biggest).
##Problem Link: https://edabit.com/challenge/gd9Yw3H4qGEt5xksN

#Examples:
#sort_nums_ascending([1, 2, 10, 50, 5]) ➞ [1, 2, 5, 10, 50]
#sort_nums_ascending([80, 29, 4, -95, -24, 85]) ➞ [-95, -24, 4, 29, 80, 85]
#sort_nums_ascending([]) ➞ []


#Solution:
def sort_nums_ascending(lst):

    #Return sorted list
    return None if lst == [] and lst == None else sorted(lst)
