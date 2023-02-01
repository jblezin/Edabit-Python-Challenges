##Problem Statement: Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
##Problem Link: https://edabit.com/challenge/gt9LLufDCMHKMioh2

#Examples:
#stutter("incredible") ➞ "in... in... incredible?"
#stutter("enthusiastic") ➞ "en... en... enthusiastic?"
#stutter("outstanding") ➞ "ou... ou... outstanding?"

#Solution:
def stutter(word):
    
    #Create containers to hold first three characters in word
    return "{}... {}... {}?".format(word[:2], word[:2], word)
