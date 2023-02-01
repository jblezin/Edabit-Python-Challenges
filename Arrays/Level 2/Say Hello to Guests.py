##Problem Statement: In this exercise you will have to:
#1. Take a list of names.
#2. Add "Hello" to every name.
#3. Make one big string with all greetings.
#The solution should be one string with a comma in between every "Hello (Name)".
##Problem Link: https://edabit.com/challenge/SKorutJdWGBzXJDRt

#Examples:
#greet_people(["Joe"]) ➞ "Hello Joe"
#greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"
#greet_people(["Frank", "Angela", "Joe"]) ➞ "Hello Frank, Hello Angela, Hello Joe"

#Solution:
def greet_people(names):

    
    return ', '.join(["Hello " + element for element in names])
