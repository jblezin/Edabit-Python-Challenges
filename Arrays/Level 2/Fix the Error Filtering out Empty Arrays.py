##Problem Statement: Fix my code so that all tests pass.
##Problem Link: https://edabit.com/challenge/raN9mCseAYJvoJQtQ

#Examples:
# What I want:
#remove_empty_arrays([1, 2, [], 4]) ➞ [1, 2, 4]

#The Code Tab
#def remove_empty_arrays(arr):
#        return [x for x in arr if len(x) != 0]


# What I am getting:
#ERROR: Traceback:
#   in <module>
#   in remove_empty_arrays
#   in <listcomp>
#TypeError: object of type 'int' has no len()

#Solution:
def remove_empty_arrays(arr):

    return [x for x in arr if x != []]
