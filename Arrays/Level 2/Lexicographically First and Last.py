##Problem Statement: Write a function that returns the lexicographically first and lexicographically last rearrangements of a lowercase string. Output the results in the following manner:
##Problem Link: https://edabit.com/challenge/xW6X8cQSHrcjpTXsn

#Examples:
#first_and_last("marmite") ➞ ["aeimmrt", "trmmiea"]
#first_and_last("bench") ➞ ["bcehn", "nhecb"]
#first_and_last("scoop") ➞ ["coops", "spooc"]

#Solution:
def first_and_last(string:

    #Return list of storted string
    return [''.join(sorted(string)) , ''.join(sorted(string))[::-1]]
