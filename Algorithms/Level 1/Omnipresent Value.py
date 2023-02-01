##Problem Statement:Omnipresent Value
##Problem Link: https://edabit.com/challenge/cqucnDiDA5J5vjGAJ

#A value is omnipresent if it exists in every sublist inside the main list.

#To illustrate:
#[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
#3 exists in every element inside this list, so is omnipresent.

#Examples:
#is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ True
#is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ False
#is_omnipresent([[5], [5], [5], [6, 5]], 5) ➞ True
#is_omnipresent([[5], [5], [5], [6, 5]], 6) ➞ False

#Solution:
def is_omnipresent(list, value):

    #Search for given value in each element in list
    return all([value in element for element in list])
