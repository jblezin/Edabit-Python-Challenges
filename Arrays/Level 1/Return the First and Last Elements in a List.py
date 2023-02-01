##Problem Statement: Create a function that takes a list of values and returns the first and last values in a new list.
##Problem Link: https://edabit.com/challenge/9kkSyfN62E4At9wcy

#Examples:
#first_last([5, 10, 15, 20, 25]) ➞ [5, 25]
#first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True]
#first_last([None, 4, "6", "hello", None]) ➞ [None, None]

#Solution:#
def first_last(lst):

    #Return first & last element in list
    return [lst[0] ,lst[-1]]
