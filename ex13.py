# What is the python module set? How many are there? What functions do they serve? I am going to google them right now. I was able to fing modules that can do presentations to games to web development. I wasn't specifically able to find the name sys. Perhaps It is contained in a different one I don't know. Gee, I wish I have a genie to answer the questions that pop up in my mind. Sriram Enga da irukke?
from sys import argv # I tried to change the name of the argument variable to some other name such as argv1. Pythoon gave me an error. I am able to fullly understand what an argument variable, and how it takes in values that I input inside the terminal. Hopefully things will get clearer soon. What is an argument variable and how is it different from raw_input()? raw_input takes values from inside the program after it is executed, but in this case the values are issued from the command line itself. 

# Modules, libraries I feel are one and the same. These words are used intechangibly. 

script, first, second, thirdly, fourth, fifth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", thirdly # Changing the names of the variables inside the program seem to work. such as changing third to thirdly. Is argv predefined in Python and can be used only in that sense. I don't know.
print "4th variable", fourth
print "5th variable ", fifth
var1 = raw_input('This is raw input ')
var2 = raw_input('This is another raw input ')
print var1, '\n',  var2 # I also learnt that when using print statement we need to seperate entities using commas, otherwise it throws up an error. Without using \n escape sequence can we print in the same line? I do not know.
