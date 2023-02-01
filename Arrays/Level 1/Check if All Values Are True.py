##Problem Statement: Create a function that returns True if all parameters are truthy, and False otherwise.
##Problem Link: https://edabit.com/challenge/ogjDWJAT2kTXEzkD5

#Examples:
#all_truthy(True, True, True) ➞ True
#all_truthy(True, False, True) ➞ False
#all_truthy(5, 4, 3, 2, 1, 0) ➞ False

#Solution:#
def all_truthy(*args):
  
  #Create empty list
  lst = []
  
  #Loop & append to list
  for x in args:
    lst.append(x)
  
  #Return True if each element is the same
  return all(lst)
