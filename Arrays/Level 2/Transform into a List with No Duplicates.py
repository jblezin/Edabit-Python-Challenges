##Problem Statement: A set is a collection of unique items. A set can be formed from a list by removing all duplicate items.
##Problem Link: https://edabit.com/challenge/hFNhDGNt8CNjSNnG9

#Examples:
#setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
#setify([4, 4, 4, 4]) ➞ [4]
#setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
#setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]

#Solution:
def setify(lst):

    #Return sorted list without duplicates
    return sorted(set(lst))
