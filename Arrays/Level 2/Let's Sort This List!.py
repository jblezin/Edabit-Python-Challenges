##Problem Statement: Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:
#"Asc" returns a sorted list in ascending order.
#"Des" returns a sorted list in descending order.
#"None" returns a list without any modification.
##Problem Link: https://edabit.com/challenge/NM8JbG5K2ajKjkqpj

#Examples:
#asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]
#asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]
#asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]

#Solution:
def asc_des_none(lst, order):

    #Return sorted list on given order
    return  (order if s == "None" else (sorted(order) if s == 'Asc' else sorted(order, reverse=True)))
