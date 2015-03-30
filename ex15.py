from sys import argv # Readinng the filename using argv from the terminal

script, filename = argv

txt = open(filename) # open fuction apparently returns a file object, Whatever that means. File object is like whole bunch of information on a file, its name, how you want to open it etcetera etcetera. You can access its different features using different functions. I wonder if open function can only be used to return files, can it be used for something else.

print "Here's your file %r:" % filename
print "%s" % txt.read() # This read function returns the data in the file as a string until EOF(End of file) is reached.
txt.close() # closing of the file. This is also a file operation function. Notice here that the variable txt is a file object and we can call the read functionon it. Also notice the weird way how this function call works. Fileobject.function(). Some file functions return a value, and some don't. Remember that for now.

print "Type the filename again:"
file_again = raw_input('> ') # Using a prompt in raw_input() 

txt_again = open(file_again) # Using a different variable to store the file object. 

print txt_again.read()
txt_again.close()
