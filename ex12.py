age = raw_input('How old are you? ') # This code does what i discussed in the previous program. We are giving a prompt statement inside the raw_input function to prompt the user to enter a value.
height = raw_input('What\'s your height? ') # When i Hit ^D (cntrl D) it throws up a EOF error. I think ^D in unix is for giving a blank line and go to the next line. 
weight = raw_input('What\'s your weight? ')

print "You are %r years old, %r tall, %r heavy." % (age, height, weight) # the output actually shows the slash after 6'2" I was using two single quotes instead of the double quote to type inches. Since they are different I think python shows the escape sequence.
