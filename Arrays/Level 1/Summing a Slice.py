##Problem Statement: Given a list and an integer n, return the sum of the first n numbers in the list.
##Problem Link: https://edabit.com/challenge/6Pf5GGG6HnzbB95gf

#Examples:
#sum_first_n_nums([1, 3, 2], 2) ➞ 4
#sum_first_n_nums([4, 2, 5, 7], 4) ➞ 18
#sum_first_n_nums([3, 6, 2], 0) ➞ 0


#Solution:
def sum_first_n_nums(lst, n):

    #Return sum of range
    return  sum(lst[:n])
