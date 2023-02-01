##Problem Statement: Write a function that returns the number of users in a chatroom based on the following rules:
#If there is no one, return "no one online".
#If there is 1 person, return "user1 online".
#If there are 2 people, return "user1 and user2 online".
#If there are n>2 people, return the first two names and add "and n-2 more online".

##Problem Link: https://edabit.com/challenge/PwGFjiSG3kXzp8rjw

#Examples:
#chatroom_status([]) ➞ "no one online"
#chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"
#chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"
#chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])➞ "pap_ier44, townieBOY and 4 more online"

#Solution:
def chatroom_status(users):
  if len(users) == 0:
    return "no one online"
  elif len(users) == 1:
    return  "{} online".format(users[0])
  elif len(users) == 2:
    return "{} and {} online".format(users[0],users[1])
  elif len(users) > 2:
    return "{}, {} and {} more online".format(users[0],users[1],len(users) - 2)
