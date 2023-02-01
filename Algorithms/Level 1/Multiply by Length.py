##Problem Statement: Create a function to multiply all of the values in a list by the amount of values in the given list.
##Problem Link: https://edabit.com/challenge/2kz9W4tqZyCNCAhik

#Examples:
#multiply_by_length([2, 3, 1, 0]) ➞ [8, 12, 4, 0]
#multiply_by_length([4, 1, 1]) ➞ ([12, 3, 3])
#multiply_by_length([1, 0, 3, 3, 7, 2, 1]) ➞  [7, 0, 21, 21, 49, 14, 7]
#multiply_by_length([0]) ➞ ([0])

#Solution:
def MultiplyByLength(list):
    
    #Find length of list & mupltipy by each element in list
    return [element * len(list) for element in list]
