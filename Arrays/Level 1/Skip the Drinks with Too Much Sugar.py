##Problem Statement: Write a function that takes a list of drinks and returns a list of only drinks with no sugar in them. Drinks that contain sugar (in this challenge) are:
#1. cola
#2. fanta
##Problem Link: https://edabit.com/challenge/vgbrdMw85i4C5sgS8

#Examples:
#skip_the_sugar(["fanta", "cola", "water"]) ➞ ["water"]
#skip_the_sugar(["fanta", "cola"]) ➞ []
#skip_the_sugar(["lemonade", "beer", "water"]) ➞ ["lemonade", "beer", "water"]


#Solution:
def skip_the_sugar(drinks):
    
    #Remove 'cola'
    if 'cola' in drinks:
        drinks.remove('cola')
        
    #Remove 'fanta'
    if 'fanta' in drinks:
        drinks.remove('fanta')
        
    return drinks
