##Problem Statement: Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.
##Problem Link: https://edabit.com/challenge/LMjficQtWW36a3by3

#Examples:
#probability([5, 1, 8, 9], 6) ➞ 50.0
#probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7
#probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0

#Solution:
def probability(lst, n):

    #Return probability of selecting an element greater than or = to n
    return round(len([element for element in lst if element >= n]) / len(lst) * 100,1)
