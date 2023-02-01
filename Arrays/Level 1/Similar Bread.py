##Problem Statement: Given two lists, which represent two sandwiches, return whether both sandwiches use the same type of bread. The bread will always be found at the start and end of the list.
##Problem Link: https://edabit.com/challenge/GuoJCiRJkr9CLRqJa

#Examples:
#has_same_bread(["white bread", "lettuce", "white bread"],["white bread", "tomato", "white bread"]) ➞ True
#has_same_bread(["brown bread", "chicken", "brown bread"],["white bread", "chicken", "white bread"]) ➞ False
#has_same_bread(["toast", "cheese", "toast"],["brown bread", "cheese", "toast"]) ➞ False

#Solution:
def has_same_bread(lst1, lst2):

    #Return True if both list comparison
    return lst1[0] == lst2[0] and lst1[-1] == lst2[-1]
