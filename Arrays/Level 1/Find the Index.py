##Problem Statement: Create a function that takes a list and a string as arguments and returns the index of the string.
##Problem Link: https://edabit.com/challenge/zFmJTah4E9mxJyoFF

#Examples:
#find_index(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2
#find_index(["Red", "blue", "Blue", "Green"], "blue") ➞ 1
#find_index(["a", "g", "y", "d"], "d") ➞ 3
#find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") ➞ 0


#Solution:
def find_index(lst, text):

    return lst.index(text)
