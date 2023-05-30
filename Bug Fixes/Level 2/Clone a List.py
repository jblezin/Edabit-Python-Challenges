##The Code tab has code which attempts to add a clone of a list to itself. There is no error message, but the results are not as intended. Can you fix the code?

##Problem Link: https://edabit.com/challenge/k8X82wXfFsNKfyPFT

#Examples:

#clone([1, 1]) ➞ [1, 1, [1, 1]]
#clone([1, 2, 3]) ➞ [1, 2, 3, [1, 2, 3]]
#clone(["x", "y"]) ➞ ["x", "y", ["x", "y"]]

#Solution:
def clone(lst):
    lst.append(lst[:])
    return lst
