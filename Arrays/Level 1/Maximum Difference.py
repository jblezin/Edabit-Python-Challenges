##Problem Statement: Given a list of integers, return the difference between the largest and smallest integers in the list.
##Problem Link: https://edabit.com/challenge/6fx8iNCHETW8KqAui

#Examples:
#difference([10, 15, 20, 2, 10, 6]) ➞ 18
#20 - 2 = 18

#difference([-3, 4, -9, -1, -2, 15]) ➞ 24
#15 - (-9) = 24

#difference([4, 17, 12, 2, 10, 2]) ➞ 15

#Solution:
def difference(numbers):
    
    #Return difference between largest & smallest integer in list
    return max(numbers) - min(numbers)
