##Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.

##Problem Link: https://edabit.com/challenge/YzcnFjMEKQfyHAg6B

#Examples:
#simon_says([1, 2], [5, 1]) ➞ True
#simon_says([1, 2], [5, 5]) ➞ False
#simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
#simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False

#Solution:
def simon_says(lst1, lst2):
  return lst1[:-1] == lst2[1:] 
