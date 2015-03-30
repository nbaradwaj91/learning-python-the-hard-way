x = "There are %d types of people." % 10 # Formatting variables to put into a string.  
binary = "binary" # Usual string variable
do_not = "don't" # Ditto
y = "Those who know %s and those who %s." % (binary, do_not) # Same as line 1 but instead of using numbers directly we use the variables that are storing integer values. Basically this % thing is used for including variables into the string. But because you can't use them directly we 'format' them into the right style that is correct.

print x # usual print command
print y # same as the previous line

print "I said: %r." % x # %r is the same as %s I think, I am not sure, probably I will learn more about it in the following lessons. AFAIK %r converts the variable x into a string using some technique, %s also does the same but uses a different technique. Hopefully stuff will become less murkier as time moves on. 
print "I also said: '%s'." % y # Same thing happening here.
hilarious = False # This is set to a Boolean value, viz. True or False. I wonder if there are any more boolean types other than true or false.
joke_evaluvation = "Isn't that joke so funny?! %r"

print joke_evaluvation # As I expected this prints out with a %r actually appended to the the string. 

print joke_evaluvation % hilarious # Since the %r is already appended inside the string this gives the stuff that %r refers to which is hilarious. I am guessing that the False that is stored as a boolean is converted to a string before appending to the string joke evaluvation

w = "This is the left side of ..." # this is a string
e = "a string with a right side." # same thing

print w+e # The + between two strings just attaches the strings together. What I also noticed is that the attachment does not include any space between the two strings. I wonder what will happen if we try to add a string and a number together. Lets try it out.

# print w+10 This throws up an error saying, cannot concatenate str and int type objects. Fair enough.  
