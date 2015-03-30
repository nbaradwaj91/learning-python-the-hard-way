# usual import from sys module
from sys import argv 

script, input_file = argv
# function defenition print_all using f is passed as a file object. Inside we call the read function associated with f
def print_all(f):
	print f.read()
# Once we call f.read() it reads all values as a string from the file till it encounters EOF. After doing its job it does not do anything to the position of the file pointer.
def rewind(f):
	f.seek(0)
# The readline functions reads the file until EOL is encountered. The file pointer is then automatically set to the succeeding line. Here 
def print_a_line(line_count, f):
	print line_count, f.tell(), f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print"Let's print three lines."

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# Always remember to close your files. 
current_file.close()
