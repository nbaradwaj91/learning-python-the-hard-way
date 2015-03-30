print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input('type here') # raw_input I think from the name is just the input as typed on the console. I don't think it distinguishes from numbers to string to floating. Hopefully I will learn how. You can also modify it by giving an argument inside it such that It will display whatever the argument is before waiting for the input

print "So, you are %r years old, %r tall, and %r heavy." % (age, height, weight)
# This is supposed to print with an escape sequence next to the " but it doesn't I don't know why.

x = int(raw_input('give a value for x '))
print "The value you have given is %d" % x 
