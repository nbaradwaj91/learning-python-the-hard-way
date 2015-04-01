# the if statement executes the lines of code under it (indented) if the expression next to it is True. It skips those lines otherwise. 
# The indentation is done to make sure that the code under it comes under the influence of the if statement. Always make sure that the if is terminated by a :.
# 
people = 20
cats = 30
dogs = 15


if not((people < cats) or (people == cats)) :
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"


dogs += 5

if people >= dogs:
	print "People are greater than equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."
