# I first typed down the script then ran it. It executed and printed a whole bunch of stuff on the screen. I then went back and analysed the output and commented out the relevant code to my understanding of how python evaluvates mathematical expression. I learnt that Division > Multiplication > Remainder > Addition. I also learnt that when you compare two values, python always prints out true or false based on the expression it evaluvates. 

# Secondly, I added .0 to all the number converting them to floating points apparently. I know from my previous little programming experience that a floating point is used to describe numbers with non zero decimal places. I can also figure out that python treats 5 and 5.0 differently 5 as an integer and 5.0 as a floating point. The output for the number of eggs channged because it contained a 1 upon 4 which previously was 0 because the 4 goes 0 times in 1 (python did not know fractions existed) I then gave python the knowledge about fractions by including a .0 at the end which led to it realizing that 1 upon 4 is actually 0.25.


print "I will now count my chickens:" # prints a line

print "Hens", 25.0 + 30.0 /6.0 # prints the number of hens (using BODMAS)
print "Roosters", 100.0 -25.0 * 3.0 % 4.0 # prints the roosters multiplication first and then followed by the remainder operator which is modulo or percentage operator

print "Now I will count the eggs:" # prints out the line

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0 # division, modulo, then addition

print "Is it true that 3 + 2 < 5 - 7?" # prints out line within ""

print 3.0 + 2.0 < 5.0 - 7.0 # prints a True or False value (compares the two expression)

print "What is 3 + 2?", 3.0 + 2.0 # adds 3 and 2
print "what is 5 - 7?", 5.0 - 7.0 # subtracts 7 from 5

print "Oh, that's why it's False." # pritnts out a line within ""

print "How about some more?" # prints out a line within ""

print "Is it greater?", 5.0 < -2.0 # Prints out true or false value based on the expression this is obviously false because 5 is greater than -2
print "Is it greater or equal?", 5.0 >= -2.0 # Prints out true or false based on the expression this is true obviously because 5 is greater than or equal to -2
print "is it less ot equal?", 5.0 <= -2.0 # Prints out a true or false value based on the expression this is ovbiously false because 5 is greater than -2
 
