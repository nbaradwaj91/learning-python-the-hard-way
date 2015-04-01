formatter = "%r " * 4 # The variable formatter has a string with values %r stored in it 4 times. I wonder if %r * 4 would work? Let me try it. There is exact replacement of %r. If there were no spaces between them then that is how the ouput too will be printed. 

print formatter % (1, 2, 3, 4) # %r takes values 1 to 4 as mentioned in the order.
#print formatter % ("one", "two", "three", "four")
#print formatter % (True, False, False, True)
#print formatter % (formatter, formatter, formatter, formatter)
#print formatter % (
#	"I had this thing.",
#	"That you could type up right.",
#	"But it didn't sing.",
#	"So I said good night."
#)
# The line But it didn't sing is printed in double quotes because it already has a single quote within it. Python does not want to be confused I guess. I think the same would apply for string in single quote containing double quote within them.
formatter1 = formatter % (1, 2, 23, 2223) # I also want to know if we can assign a particular value of formatter to the variable formatter 1. I think the bigger picture here is we can use a sort of loop and can assign different values for formatter1 that are in the same format (4 objects seperated by a blank space.). See what I did there?.
print formatter1
