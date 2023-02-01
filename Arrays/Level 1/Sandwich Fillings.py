##Problem Statement: CGiven a sandwich (as a list), return a list of fillings inside the sandwich. This involves ignoring the first and last elements.
##Problem Link: https://edabit.com/challenge/T3p8AkyXcE9ALkWbA

#Examples:
#get_fillings(["bread", "ham", "cheese", "ham", "bread"]) ➞ ["ham", "cheese", "ham"]
#get_fillings(["bread", "sausage", "tomato", "bread"]) ➞ ["sausage", "tomato"]
#get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) ➞ ["lettuce", "bacon", "tomato"]


#Solution:
def get_fillings(sandwich):

    #Return ingredients between range
    return sandwich[1:-1]
