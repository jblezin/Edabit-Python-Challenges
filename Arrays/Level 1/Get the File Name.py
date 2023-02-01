##Problem Statement: Create a function that returns the selected filename from a path. Include the extension in your answer.
##Problem Link: https://edabit.com/challenge/EYojuPCtvSzF2chkZ

#Examples:
#get_filename("C:/Projects/pil_tests/ascii/edabit.txt") ➞ "edabit.txt"
#get_filename("C:/Users/johnsmith/Music/Beethoven_5.mp3") ➞ "Beethoven_5.mp3"
#get_filename("ffprobe.exe") ➞ "ffprobe.exe"


#Solution:
import os

def get_filename(path):
    
    #Return filepath
    return os.path.basename(path)
