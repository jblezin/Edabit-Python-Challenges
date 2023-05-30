##Create a function that returns the last value of the last item in a list or string.
##Problem Link: https://edabit.com/challenge/mcC546MLnBjNLXTb8

#Examples:
#last_ind([0, 4, 19, 34, 50, -9, 2]) ➞ 2
#last_ind("The quick brown fox jumped over the lazy dog") ➞ "g"
#last_ind([]) ➞ None

#Solution:
def last_ind(lst):
    return None if lst == [] or lst =='' else lst[-1]
