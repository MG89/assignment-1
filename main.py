'''This program was written by Matthew G.

It prints some text to the user.
Date Created: 09/30/2017 '''

#Prints text to the user.
print("Hello!! My name is Matthew G.")

#Input statement to read name from the user.
name = input("What is yours? ")

#Prints input and text to the user.
print("Hello ", name, "!!  I am a Computer Science student in PCC, Sylvania. "
        "I am very Excited to be in this class and working with the Python language! "
        "I attend school full-time and work part-time.")

#Input statement to read status of user.
status = input("Are you a student or an instructor? ")

#Prints differnt text based on the status of the user. 
if status == "student":
    print ("A", status, "! Very cool. you are student")

elif status == "instructor":
    print ("A", status, "! Very cool. you are instructor")

else:
    print("Well that's no fun.") 

#Prints text to the user.
print("Hello World!!!")
