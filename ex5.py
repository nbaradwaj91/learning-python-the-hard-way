# use of something called formaters. I know what the word means. I don't actually know what a formatter is. I can deduce that the %s, %d is replaced by the variables mentioned after the % symbol. I also know that %s is for string and %d is for numbers. I don't know how this will vary for whole numbers and floating point numbers. Let me try it out. No I don't think %d works for floating point. The number is displayed as only 25 ignoring the .32 part. I have to learn what is itfor floating points. One more thing I noticed is that in long comments such as these, when you are in the last line of the comment, pressing the up arrow goes to the first line of the comment and not the previous line. Is there a way out? Is the stuff after the # treated as a single line, even though it may be displayed as multiple lines? I don't know. I have to ask some expert or search online. Ialso have to learn about various types of formatters, which I am going to do right now. The %d and %i are the same thing both is for integer decimal values. %e is for floating point scientific notation. %E is also scientific notation but with E instead of e while printing the number. For floating point values, the formatter is %f or %F. %r is also for string but it converts the evaluvated expression into a string format. I am not too sure about this. Hopefully this is what it does and I can learn more about it later. %g prints only the required amount offloating point numbers after the decimal point does not fill up with zeros. When I try to remove the my_ prefix from the variable names, in the my_float variable the colour changed. I am thinking this name float is already used in python and I can't name a variable named float. My learnings.    

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
heightincm = height * 2.54
weight = 180 # lbs
weightinkg = weight * 0.453592
ffloat = 25.32
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "weight in kg is %g." % weightinkg
print "Height in centimeters is %g." % heightincm

#this line is tricky, try to get it exactly right
print "If I add %d %d %d and %f I get %g." % (age, height, weight, ffloat, age+ height + weight + ffloat)
