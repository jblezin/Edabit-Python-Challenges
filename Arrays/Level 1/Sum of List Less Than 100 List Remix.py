##Problem Statement: Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.
##Problem Link: https://edabit.com/challenge/HRu9WggWxdSpYjxNf

#Examples:
#list_less_than_100([5, 57]) ➞ True
#list_less_than_100([77, 30]) ➞ False
#list_less_than_100([0]) ➞ True

#Solution:
def list_less_than_100(list):

    #Return True if sum of integers is less than 100
    return sum(list) < 100
