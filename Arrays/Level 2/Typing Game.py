##Problem Statement: You're in the midst of creating a typing game.
#Create a function that takes in two lists: the list of user-typed words, and the list of correctly-typed words and outputs a list containing 1s (correctly-typed words) and -1s (incorrectly-typed words).
##Problem Link: https://edabit.com/challenge/DQy6FL26FeNDecqNr

#Examples:
#correct_stream(["it", "is", "find"], ["it", "is", "fine"]) ➞ [1, 1, -1]
#correct_stream(["april", "showrs", "bring", "may", "flowers"], ["april", "showers", "bring", "may", "flowers"]) ➞ [1, -1, 1, 1, 1]

#Solution:
def correct_stream(user, correct):

    #List of misspelled words
    return [1 if element1 == element2 else -1 for element1, element2 in zip(user, correct)]
