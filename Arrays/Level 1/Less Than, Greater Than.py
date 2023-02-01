##Problem Statement: Create a function that takes two numbers num1, num2, and a list lst and returns a list containing all the numbers in lst greater than num1 and less than num2.
##Problem Link: https://edabit.com/challenge/HJNhLoS4W8jdEYprh

#Examples:
#list_between(3, 8, [1, 5, 95, 0, 4, 7]) ➞ [5, 4, 7]
#list_between(1, 10, [1, 10, 25, 8, 11, 6]) ➞ [8, 6]
#list_between(7, 32, [1, 2, 3, 78]) ➞ []

#Solution:
def list_between(num1, num2, lst):
  
  #Create empty list
  lst1 =[]
  
  #Loop through lst & append element greater than num1 & num2
  for x in lst:
    if num1 <  x < num2:
      lst1.append(x)
 
  return lst1
