##Python has three main types of data structures formed by smaller objects:

#Lists, written with [] square brackets, such as [1, 2, 4, 8].
T#uples, written with () parentheses, such as (7, 8, 9).
S#ets, written with{} curly brackets, such as {2, 3, 5, 7, 11, 13}.
#Each of these types has its own special properties and peculiarities that are worth knowing, but this challenge is only about transforming these data types into each other.

#This can be done as in the following:

#tuple([1,2,4,8]) returns (1,2,4,8)
#list({2,3,5,7,11}) returns [2, 3, 5, 7, 11, 13]
#set((1,2,4)) returns {1,2,4}
#Given two data structures, data1 and data2, return data2 converted to the type of data1.

##Problem Link: https://edabit.com/challenge/GPRZauknkEbyRz5qM

#Examples:
#convert([1, 2, 4, 8], (7, 8, 9)) ➞ [7, 8, 9]
#convert((7, 8, 9), [1, 2, 4, 8]) ➞ (1, 2, 4, 8)
#convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}) ➞ [2, 3, 5, 7, 11, 13]
#convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]) ➞ {8, 1, 2, 4}

#Solution:
def convert(data1, data2):
  if type(data1) == set:
    return set(data2)
  if type(data1) == list:
    return list(data2)
  else:
    return tuple(data2)
