##Problem Statement: Create a function that takes a list of numbers and returns the sum of its cubes.
##Problem Link: https://edabit.com/challenge/h4SrMDnwPpmotn2cZ

#Examples:
#sum_of_cubes([1, 5, 9]) ➞ 855 Since 1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855
#sum_of_cubes([3, 4, 5]) ➞ 216
#sum_of_cubes([2]) ➞ 8
#sum_of_cubes([]) ➞ 0

#Solution:
def sum_of_cubes(numbers):
  
  #Cube each element in list, then sum all results
  return sum([element ** 3 for element in numbers])
