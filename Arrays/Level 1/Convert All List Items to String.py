##Problem Statement: Create a function that takes a list of integers and strings. Convert integers to strings and return the new list.
##Problem Link: https://edabit.com/challenge/7ujabrnbRK9w6Z5xb

#Examples:
#parse_list([1, 2, "a", "b"]) ➞ ["1", "2", "a", "b"]
#parse_list(["abc", 123, "def", 456]) ➞ ["abc", "123", "def", "456"]
#parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]) ➞ ["1", "2", "3", "17", "24", "3", "a", "123b"]
#parse_list([]) ➞ []

#Solution:#
def parse_list(lst):
    
    #Return list of elements as a string
    return [str(x) for x in lst]
