# code introduces lists and loops. There is some logic behind this because you can access elements of a list with the help of loops. There is a weird way how loops work in python. You can pass an object as an iterator. Hopefully I understand how it works.
# lists can contain different data types.
the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# I don't understand how loops work. The loop variable gives out the list elements. However we can also access it as an index. If i give list[i] then also list elements will be printed. Interesting.
for number in the_count:
	print "This is count %d." % number

for fruit in fruits:
	print "A fruit of type %s." % fruit


for i in change:
	print "I got %r." % i

elements = []

# the range function. It returns a list of elements from the first number to last number -1 I think it can also take the artithmetic common difference also as a parameter.
for i in range(0, 6):
	print "Adding %d to the list." % i
	elements.append(i)

print i
for i in elements:
	print i
	print "Element was: %r." % elements

