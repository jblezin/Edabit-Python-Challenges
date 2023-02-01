##Problem Statement: Create a function to calculate how many characters in total are needed to make up the shape. You will be given a list of strings which make up a shape in the compiler (i.e. a square, a rectangle or a line).
##Problem Link: https://edabit.com/challenge/S9KCN5kqoDbhNdKh5

#Examples:
#count_characters(["###", "###","###"]) ➞ 9
#count_characters(["22222222", "22222222", ]) ➞ 16
#count_characters(["------------------"]) ➞ 18
#count_characters([]) ➞ 0
#count_characters(["", ""]) ➞ 0

#Solution:
def count_characters(lst):

    #Return count of all elements in list
    return sum(len(element) for element in lst)
