##Problem Statement: Write a function that retrieves the last n elements from a list.
##Problem Link: https://edabit.com/challenge/HBKAGJZ62JkCTgYX3

#Examples:
#last([1, 2, 3, 4, 5], 1) ➞ [5]
#last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
#last([1, 2, 3, 4, 5], 7) ➞ "invalid"
#last([1, 2, 3, 4, 5], 0) ➞ []

#Solution:
def last(a, n):

    #Return the last Nth element(s) for list
    return ("invalid" if n > len(a) else ( [] if n == 0 else a[n *-1:]))
