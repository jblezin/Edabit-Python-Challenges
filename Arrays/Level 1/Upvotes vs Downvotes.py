##Problem Statement: Given a dictionary containing counts of both upvotes and downvotes, return what vote count should be displayed. This is calculated by subtracting the number of downvotes from upvotes.
##Problem Link: https://edabit.com/challenge/SFE4q5pFTi8TBwj76

#Examples:
#get_vote_count({ "upvotes": 13, "downvotes": 0 }) ➞ 13
#get_vote_count({ "upvotes": 2, "downvotes": 33 }) ➞ -31
#get_vote_count({ "upvotes": 132, "downvotes": 132 }) ➞ 0


#Solution:
def get_vote_count(votes):

    #Return difference between both dictionary values
    return votes["upvotes"] - votes["downvotes"]
