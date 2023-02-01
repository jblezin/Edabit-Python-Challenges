##Problem Statement: Create a function that filters out a list to include numbers that only have a certain number of digits.
##Problem Link: https://edabit.com/challenge/WAyXZpuqxtXG9swb3

#Examples:
#filter_digit_length([88, 232, 4, 9721, 555], 3) ➞ [232, 555]
# Include only numbers with 3 digits.

#filter_digit_length([2, 7, 8, 9, 1012], 1) ➞ [2, 7, 8, 9]
# Include only numbers with 1 digit.

#filter_digit_length([32, 88, 74, 91, 300, 4050], 1) ➞ []
# No numbers with only 1 digit exist => return empty list.

#filter_digit_length([5, 6, 8, 9], 1) ➞ [5, 6, 8, 9]
# All numbers in the list have 1 digit only => return original list.

#Solution:
def filter_digit_length(lst, number):

    #Return elements with length of numbers
    return [element for element in lst  if len(str(element)) == number]
