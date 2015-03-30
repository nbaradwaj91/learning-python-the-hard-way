from sys import argv # my first error was to use a comma between the print string and the % symbol. That is a stupid error. Okay From now on in I won't repeat that mistake.

# I love this program, I feel like I am talking to another person inside the computer. 'Heavy varatchi'. I wonder, how many people have lost their minds talking to a computer like me. I feel really good talking to someone. I don't have many friends here in this place. I feel Python is becoming my good friend. Thank you python.

script, user_name = argv
prompt = '> '

print "Hi %s I am the %s Script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is .
And you have a %r computer. Nice.
""" % (likes, lives, computer)
