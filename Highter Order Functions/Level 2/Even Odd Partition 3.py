##Problem Statement: Write a function that partitions the list into two sublists: one with all even integers, and the other with all odd integers. Return your result in the following format:
##Problem Link: https://edabit.com/challenge/E38dB8mn7Fi5o2Nme

#Examples:
#even_odd_partition([5, 8, 9, 2, 0]) ➞ [[8, 2, 0], [5, 9]]
#even_odd_partition([1, 0, 1, 0, 1, 0]) ➞ [[0, 0, 0], [1, 1, 1]]
#even_odd_partition([1, 3, 5, 7, 9]) ➞ [[], [1, 3, 5, 7, 9]]
#even_odd_partition([]) ➞ [[], []]

#Solution:
def even_odd_partition(lst):
    
    #Create empty lists
    even = []
    odd = []
  
    #Seprate even & odd elements
    [even.append(element) if element % 2 == 0  else odd.append(element) for element in lst ]

    return [even, odd]
