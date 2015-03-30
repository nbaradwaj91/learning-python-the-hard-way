# Function defined here using the def command and takes a couple of arguments. It then prints out a buch of outputs using the value of the arguments. Always remember to end function defenition with a :   
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Thats Enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# Function call here, Same name as the function defeniton arguments within paranthesis
cheese_and_crackers(20,30) 


print "Or we can use variables from our script."
amount_of_cheese = 10
amount_of_crackers = 50
# function call using variables in the script. One of many ways of making the function call
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Function call using input provided from the user. Notice the conversion from string to integer. So that we can add them. It wouldn't have mattered if we had not converted them in this case because we are't doing any mathematical operations on them. We are only displaying them as it is.
# Actually the integer conversion is important because, in the function defenition we have used the format modifier %d, which is integer. It was wrong of me to think that it wouldn't have mattered. If we had used %s or %r then it wouldn't have. But then we also couldn't have carried out mathematical operations on them.
cheese_and_crackers(int(raw_input('> ')), int(raw_input('> ')))
