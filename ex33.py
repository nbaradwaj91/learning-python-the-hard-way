# one major difference between while loop and for loop is the loop increment is done in 
def whileloop(index, increment):
	numbers = []

	for i in range(0, index, increment):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

	print "The numbers:"

	for num in numbers:
		print num

index = int(raw_input("Enter the loop variable"))
increment = int(raw_input("Enter the increment"))
whileloop(index, increment)
