##Problem Statement: Programmer Pete is trying to combine two lists inside one list into one without changing the order of the list nor the type and because he's pretty advanced he made it without blinking, but I want you to make it, too.
##Problem Link: https://edabit.com/challenge/YK9PpDRfyBTEarNyR

#Examples:
#one_list([[1, 2], [3, 4]]) ➞ [1, 2, 3, 4]
#one_list([["a", "b"], ["c", "d"]]) ➞ ["a", "b", "c", "d"]
#one_list([[True, False], [False, False]]) ➞ [True, False, False, False]

#Solution:
def one_list(lst):

    #Return a combined list
    return [element for sublist in lst for element in sublist]
