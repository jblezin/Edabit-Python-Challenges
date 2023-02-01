##Problem Statement: Write a function that maps files to their extension names.
##Problem Link: https://edabit.com/challenge/MpHke3QqR4uC75rYS

#Examples:
#get_extension(["code.html", "code.css"]) ➞ ["html", "css"]
#get_extension(["project1.jpg", "project1.pdf", "project1.mp3"]) ➞ ["jpg", "pdf", "mp3"]
#get_extension(["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"]) ➞ ["rb", "cpp", "py", "js"]

#Solution:
def get_extension(lst):

    #Return file extension
    return [element.split('.')[-1] for element in lst]
