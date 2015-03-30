from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN."

raw_input('? ')

print "Opening the file..."
target = open(filename, 'r+')

print "Truncating the file. Goodbye." # Truncate as a seperate command isn't required because when we open the file in w mode, python automatically truncates the file.
target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3)) # using formats and escapes I have reduced the code into one single line. from three lines.
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
#target.close()
#target = open(filename, 'r+') # I wanted to print the contents of the file after writing the new data. I tried doing it in w+, r+ modes. I wasn't able to see anything on the screen. It didn't give me an error. So I need to figureout what is going on. When I need to print the contents should I close the file and open again? Okay, I understood, file.read returns an empty string when it encounters an EOF. Since we are already at EOF. file.read returns an empty string.
target.seek(0) # file.seek sets the current pointer at absolute. i.e. the beginning of the file.
print target.read()


print "And finally, we close it."
target.close() 
