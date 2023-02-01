##Problem Statement: Mary wants to run a 25-mile marathon. When she attempts to sign up for the marathon, she notices the sign-up sheet doesn't directly state the marathon's length. Instead, the marathon's length is listed in small, different portions. Help Mary find out how long the marathon actually is. Return True if the marathon is 25 miles long, otherwise, return False.
##Problem Link: https://edabit.com/challenge/53phFTw72XLmxJ7Jt

#Examples:
#marathon_distance([1, 2, 3, 4]) ➞ False
#marathon_distance([1, 9, 5, 8, 2]) ➞ True
#marathon_distance([-6, 15, 4]) ➞ True

#Solution:
def marathon_distance(distance):
    
    #Return True if sum of elements in list is greater than 25.
    return False if len(distance) == 0 else sum(abs(element) for element in distance) == 25
