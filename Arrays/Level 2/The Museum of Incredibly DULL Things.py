##Problem Statement: Create a function that takes a list of integers and removes the smallest value.
##Problem Link: https://edabit.com/challenge/cx7eFvQBzjauLgwgZ

#Examples:
#remove_smallest([1, 2, 3, 4, 5] ) ➞ [2, 3, 4, 5]
#remove_smallest([5, 3, 2, 1, 4]) ➞ [5, 3, 2, 4]
#remove_smallest([2, 2, 1, 2, 1]) ➞ [2, 2, 2, 1]

#Solution:
def remove_smallest(lst):
  
  #Check for integers & remove smallest
  if len(lst) >1:
    lst.remove(min(lst))
    return lst
  
  else:
  
    return []
