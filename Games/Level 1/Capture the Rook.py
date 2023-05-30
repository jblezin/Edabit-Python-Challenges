##Write a function that returns True if two rooks can attack each other, and False otherwise.
##Problem Link: https://edabit.com/challenge/TZ8J2ryBPd6i9ugqR

#Examples:
#can_capture(["A8", "E8"]) ➞ True
#can_capture(["A1", "B2"]) ➞ False
#can_capture(["H4", "H3"]) ➞ True
#can_capture(["F5", "C8"]) ➞ False

#Solution:
def can_capture(rooks):
    return rooks[0][0].startswith(rooks[1][0]) or rooks[0][1].endswith(rooks[1][1])
