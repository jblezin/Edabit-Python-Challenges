##Problem Statement: Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
##Problem Link: https://edabit.com/challenge/HvkPdhijquecKASdF

#Examples:
#get_student_names({"Student 1" : "Steve", "Student 2" : "Becky", "Student 3" : "John"}) ➞ ["Becky", "John", "Steve"]

#Solution:
def get_student_names(students):

    #Return dictionary of sorted names
    return sorted(students.values())
