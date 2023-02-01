##Problem Statement: Create a function that finds each factor of a given number n. Your solution should return a list of the number(s) that meet this criteria.
##Problem Link: https://edabit.com/challenge/6Pf5GGG6HnzbB95gf

#Examples:
#find_factors(9) ➞ [1, 3, 9]
# 9 has three factors 1, 3 and 9
#find_factors(12) ➞ [1, 2, 3, 4, 6, 12]
#find_factors(20) ➞ [1, 2, 4, 5, 10, 20]
#find_factors(0) ➞ []
# 0 has no factors


#Solution:
def find_factors(n):
    
    #Return empty list if > 1
    if n == []:
        return 1
    
    else:
        #Return fator of element
        return [element for element in range(1,n+1) if n % element == 0]
