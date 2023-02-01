##Problem Statement: Create a function that takes a list of strings and return a list, sorted from shortest to longest.
##Problem Link: https://edabit.com/challenge/93o6y6WKFpQKoDg4T

#Examples:
#sort_by_length(["Google", "Apple", "Microsoft"]) ➞ ["Apple", "Google", "Microsoft"]
#sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) ➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]
#sort_by_length(["Turing", "Einstein", "Jung"]) ➞ ["Jung", "Turing", "Einstein"]

#Solution:
def sort_by_length(list):
    
    #Sort list in ascending order by length of element.
    return sorted(list, key = len)
