##Problem Statement: Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.
##Problem Link: https://edabit.com/challenge/uPtuNNTuASzPZMQrW

#Examples:
#get_last_item([1, 2, 3]) ➞ 3
#get_last_item(["cat", "dog", "duck"]) ➞ "duck"
#get_last_item([True, False, True]) ➞ True
#get_last_item([7, "String", False]) ➞ False

#Solution:
def get_last_item(list):
    
    #Return last element in list
    return list[-1]
