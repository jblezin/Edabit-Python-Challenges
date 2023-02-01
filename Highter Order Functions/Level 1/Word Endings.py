##Problem Statement: Create a function that adds a string ending to each member in a list.
##Problem Link: https://edabit.com/challenge/TkL6GTu9QMhYnv869

#Examples:
#add_ending(["clever", "meek", "hurried", "nice"], "ly") ➞ ["cleverly", "meekly", "hurriedly", "nicely"]
#add_ending(["new", "pander", "scoop"], "er") ➞ ["newer", "panderer", "scooper"]
#add_ending(["bend", "sharpen", "mean"], "ing") ➞ ["bending", "sharpening", "meaning"]

#Solution:
def add_ending(lst, ending):

    #Return list with given ending to each element
    return [element + ending for element in lst]
