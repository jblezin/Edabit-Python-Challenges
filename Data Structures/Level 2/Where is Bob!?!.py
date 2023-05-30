##Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.

##Problem Link: https://edabit.com/challenge/fDkAuAwR4PMWZwBKs

#Examples:
#find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
#find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
#find_bob(["Jimmy", "Layla", "James"]) ➞ -1

#Solution:
def find_bob(names):
    return (names.index("Bob") if "Bob" in names else -1)
