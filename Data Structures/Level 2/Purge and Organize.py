##Given a list of numbers, write a function that returns a list that...
#Has all duplicate elements removed.
#Is sorted from least to greatest value.

##Problem Link: https://edabit.com/challenge/EZMCpHaNFg2Yfsnxx

#Examples:
#unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
#unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
#unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]

#Solution:
def unique_sort(lst):
    return sorted(set(lst))
