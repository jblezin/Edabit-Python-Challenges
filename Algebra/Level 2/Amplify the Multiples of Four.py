##Problem Statement: Create a function that takes an integer and returns a list from 1 to the given number, where: If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number). If the number cannot be divided evenly by 4, simply return the number.
##Problem Link: https://edabit.com/challenge/ASpHKyuSXZL3MjL92

#Examples:
#amplify(4) ➞ [1, 2, 3, 40]
#amplify(3) ➞ [1, 2, 3]
#amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]

#Solution:
def amplify(number):

    #For each element in list, if divisible by 4, * by 10. If not, return original element
    return [element if element % 4 != 0 else element * 10 for element in range(1, number + 1)]
