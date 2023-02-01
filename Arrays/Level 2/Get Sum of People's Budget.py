##Problem Statement: Create the function that takes a list of dictionaries and returns the sum of people's budgets.
##Problem Link: https://edabit.com/challenge/ff2R7SymbB6PfjpPm

#Examples:
#get_budgets([{ "name": "John", "age": 21, "budget": 23000 }, { "name": "Steve",  "age": 32, "budget": 40000 }, {"name": "Martin",  "age": 16, "budget": 2700 }]) ➞ 65700
#get_budgets([{ "name": "John",  "age": 21, "budget": 29000 }, { "name": "Steve",  "age": 32, "budget": 32000 }, {"name": "Martin",  "age": 16, "budget": 1600 }]) ➞ 62600

#Solution:
def get_budgets(lst):

    #Return budget for each element in dictionary
    return sum([element["budget"] for element in lst])
