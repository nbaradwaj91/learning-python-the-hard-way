people = 50
cars = 12
trucks = 123
# if statement evaluvates the block of code under it if that evaluvates to falsethen goes to the next block.
# elif is like elseif, and can be used only following an if statement. If that if evaluvates to false then goes to elif and evaluvates that. If that evaluvates to true the remainder of the elifs and the else statement is skipped.

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "Too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright let's just take the trucks."
else:
	print "Fine, let's just stay at home then."

