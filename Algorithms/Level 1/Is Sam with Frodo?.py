##Problem Statement: Sam and Frodo need to be close. If they are side by side in the list, your function should return True. If there is a name between them, return False.
##Problem Link: https://edabit.com/challenge/RvK4LTigc4jbRLJio

#Examples:
#middle_earth(["Frodo", "Sam", "Gandalf"]) ➞ True
#middle_earth(["Frodo", "Saruman", "Sam"]) ➞ False
#middle_earth(["Orc", "Sam", "Frodo", "Legolas"]) ➞ True

#Solution:
def middle_earth(list):
    
    #Search for 'Frodo' index and check before or after if index value = 'Sam'
    return list.index("Frodo") + 1  == list.index("Sam") or list.index("Frodo") - 1 == list.index("Sam")
