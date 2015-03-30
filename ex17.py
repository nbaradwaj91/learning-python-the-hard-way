from sys import argv
#from os.path import exists

script, from_file, to_file = argv
#from_file = open(from_file, 'r')
#to_file = open(to_file, 'r+')
#to_file.write(from_file.read()
#from_file.close()
#to_file.close()
open(to_file, 'w+').write( open(from_file).read()) # successfully made it one line of code. I am soooo happy. The happiness that you feel after accomplishing something that is tough is immense. Thank you python for giving me that happiness.

# I don't understand when do I need to close the files. If I try to close them now the interpreter throws up an error. I will learn this. When I read up the python documentation for import, it talks about something called the namespace. I wonder what that is? 
#to_file.close()
#from_file.close() 


'''
print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright All done."

out_file.close()
in_file.close()
'''
