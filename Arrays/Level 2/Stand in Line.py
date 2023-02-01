##Problem Statement: Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.
##Problem Link: https://edabit.com/challenge/S26tvW7BPrJsyJApt

#Examples:
#next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
#next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
#next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
#next_in_line([], 6) ➞ "No list has been selected"

#Solution:
def next_in_line(lst, num):
  
  #Check for empty list
  if len(lst) == 0:
    return "No list has been selected"
  
  #Removes first element in list & append new element
  else:
    lst.pop(0)
    lst.append(num)
  
  return lst
