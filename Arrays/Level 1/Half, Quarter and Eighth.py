##Problem Statement: Create a function that takes a number and return a list of three numbers: half of the number, quarter of the number and an eighth of the number.
##Problem Link: https://edabit.com/challenge/u68XgCZcWGphs5R54

#Examples:
#half_quarter_eighth(6) ➞ [3, 1.5, 0.75]
#half_quarter_eighth(22) ➞ [11, 5.5, 2.75]
#half_quarter_eighth(25) ➞ [12.5, 6.25, 3.125]

#Solution:
def half_quarter_eighth(number):

    #Return list of half, quarter, & eighth of given number
    return [number * .5, number * .25, number * .125]
