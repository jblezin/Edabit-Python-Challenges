##Problem Statement: Given a dict of the stolen items and a limit, return the difference between the total value of those items and the limit of the policy.
##Problem Link: https://edabit.com/challenge/PTh7tBusAZRgjAWEZ

#Examples:
#calc_diff({ "baseball bat": 20 }, 5) ➞ 15
#calc_diff({"skate": 10, "painting": 20 }, 19) ➞ 11
#calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, 400) ➞ 1

#Solution:
def calc_diff(obj, limit):

    #Return deductible between sum of stolen items & policy
    return sum(obj.values()) - limit
