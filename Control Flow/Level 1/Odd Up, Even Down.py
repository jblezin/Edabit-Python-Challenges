##Create a function that goes through the array, incrementing (+1) for each odd-valued number and decrementing (-1) for each even-valued number.

##Problem Link: https://edabit.com/challenge/Hm2m6Gg4piQ2Xe9Sa

#Examples:
#transform([1, 2, 3, 4, 5]) ➞ [2, 1, 4, 3, 6]
#transform([3, 3, 4, 3]) ➞ [4, 4, 3, 4]
#transform([2, 2, 0, 8, 10]) ➞ [1, 1, -1, 7, 9]

#Solution:
def transform(lst):
    return [element -1 if element % 2 == 0 else element + 1 for element in lst]
