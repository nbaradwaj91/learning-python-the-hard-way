# Functions in python can return values, returned values can be anything, ranging from integer to floating points to string.
def add(a,b):
	print "Adding %d + %d." % (a, b)
	return a+b

def subtract(a, b):
	print "Subtracting %d - %d." % (a, b)
	return a-b

def multiply(a, b):
	print "Multiplying %d * %d." % (a, b)
	return a*b

def divide(a, b):
	print "Dividing %d / %d." % (a, b)
	return a/b


print "Lets do some math using functions."

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."
# python reads functions inside-out. That just means just substitutes values for functions. values are those that are returned by the function. 
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?" 

prompt = '> '

# Six lines for input? No that's far too long. How can I make it shorter?
print "Enter six numbers."
a = int(raw_input(prompt))
b = int(raw_input(prompt))
c = int(raw_input(prompt))
d = int(raw_input(prompt))
e = int(raw_input(prompt))
f = int(raw_input(prompt))

# if a and b are integers, can the values of a/b be non-integral such as floats?
answer = subtract(a, add(multiply(b, divide(c, d)),  multiply(d, divide(e,f))))
print "This is the final puzzle.", answer
