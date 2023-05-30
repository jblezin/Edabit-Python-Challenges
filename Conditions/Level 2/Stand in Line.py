##Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.

##Problem Link: https://edabit.com/challenge/S26tvW7BPrJsyJApt

#Examples:
#relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
#relation_to_luke("Leia") ➞ "Luke, I am your sister."
#relation_to_luke("Han") ➞ "Luke, I am your brother in law."

#Solution:
#next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
#next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
#next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
#next_in_line([], 6) ➞ "No list has been selected"
