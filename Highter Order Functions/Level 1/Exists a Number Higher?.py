##Problem Statement: Write a function that returns True if there exists at least one number that is larger than or equal to n.
##Problem Link: https://edabit.com/challenge/ZB25oqbEQnjijbwse

#Examples:
#exists_higher([5, 3, 15, 22, 4], 10) ➞ True
#exists_higher([1, 2, 3, 4, 5], 8) ➞ False
#exists_higher([4, 3, 3, 3, 2, 2, 2], 4) ➞ True
#exists_higher([], 5) ➞ False

#Solution:
def exists_higher(lst, number):

    #Check for empty list
    if lst == []:
        return False
    #Return True if an element is greater than number
    if number <= max(lst):
        return True
    
    else:
        return False
