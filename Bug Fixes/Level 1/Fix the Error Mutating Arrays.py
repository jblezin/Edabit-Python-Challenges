##Suppose I want to define a function that removes the last element of a list each time I call it, but does not mutate the original list. Fix the code so that the results are no longer mutating the list.

##Problem Link: https://edabit.com/challenge/tRM2zKPMezqLnXyCx

#Examples:
#def minus_one(lst):
#  arr.pop()
#  return arr

#x = [1, 2, 3, 4, 5]
#minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
#minus_one(x) ➞ [1, 2, 3]  # 2nd time function is called.
#minus_one(x) ➞ [1, 2]  # 3rd time function is called.
#minus_one(x) ➞ [1]  # 4th time function is called.

# What I want instead:
#minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
#minus_one(x) ➞ [1, 2, 3, 4]  # 2nd time function is called.
#minus_one(x) ➞ [1, 2, 3, 4]  # 3rd time function is called.
#minus_one(x) ➞ [1, 2, 3, 4]  # 4th time function is called.

#Solution:
def minus_one(lst):
    return lst[:-1]
