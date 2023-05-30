##Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

##Problem Link: https://edabit.com/challenge/eJLwXpuaffjFnzENN


#Examples:
#find_even_nums(8) ➞ [2, 4, 6, 8]
#find_even_nums(4) ➞ [2, 4]
#find_even_nums(2) ➞ [2]


#Try to use list comprehensions in your solution. Here's an example:

vals = [expression
  for value in collection
    if condition]

#This is equivalent to:

vals = []
for value in collection:
  if condition:
    vals.append(expression)



#Solution:
def find_even_nums(num):
    return [element for element in range(1,num + 1) if element % 2 ==0]
