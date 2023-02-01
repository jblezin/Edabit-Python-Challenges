##Problem Statement: Create a function that returns only strings with unique characters.
##Problem Link: https://edabit.com/challenge/GXgsHZ9emoW5bhxhh

#Examples:
#filter_unique(["abb", "abc", "abcdb", "aea", "bbb"]) ➞ ["abc"]
# "b" occurs in "abb" more than once, "b" occurs in "abcdb" more than once, etc.
#filter_unique(["88", "999", "989", "9988", "9898"]) ➞ []
#filter_unique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]) ➞ ["ABCDE", "BED", "BAC"]

#Solution:
def filter_unique(lst):
    
    #Return unique elements only
    return [element for element in lst if len(set(element)) == len(element)]
