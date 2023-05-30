##Create a function that returns the sum of all even elements in a 2D matrix.

##Problem Link: https://edabit.com/challenge/MbPpxYWMRihFeaNPB

#Examples:
#sum_of_evens([
#  [1, 0, 2],
#  [5, 5, 7],
#  [9, 4, 3]
#]) ➞ 6

#// 2 + 4 = 6

#sum_of_evens([
#  [1, 1],
#  [1, 1]
#]) ➞ 0

#sum_of_evens([
#  [42, 9],
#  [16, 8]
#]) ➞ 66

#sum_of_evens([
#  [],
#  [],
#  []
#]) ➞ 0

#Solution:
def sum_of_evens(lst):
    return sum([value for element in lst for value in element if value % 2 == 0])
