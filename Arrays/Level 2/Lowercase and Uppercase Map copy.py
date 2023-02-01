##Problem Statement: Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
##Problem Link: https://edabit.com/challenge/pimnBHXJNtQffq4Cf

#Examples:
#mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
#mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
#mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

#Solution:
def mapping(letters):

    #Returns a dictionary from elements in list
    return {element : element.title() for element in letters}
