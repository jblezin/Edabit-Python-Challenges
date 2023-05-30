##Help fix all the bugs in the function increment_items! It is intended to add 1 to every element in the list!

##Problem Link: https://edabit.com/challenge/mwGt38m3Q3KcsSaPY

#Examples:

#increment_items([0, 1, 2, 3]) ➞ [1, 2, 3, 4]
#increment_items([2, 4, 6, 8]) ➞ [3, 5, 7, 9]
#increment_items([-1, -2, -3, -4]) ➞ [0, -1, -2, -3]

#Solution:
def increment_items(lst):
    return [x + 1 for x in lst]
