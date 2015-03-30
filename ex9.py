days = "Mon Tue Wed Thu Fri Sat Sun" # Normal string
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # String with \n inbetween. I guess that the \n is for the nextline. Its great that you can store variables in the way that you want to print them. If there were no \n then it would have been printed in the same line. But if we include a \n we go to the next line

print "Here are the days: ", days # Normal way of printing a string and then a variable
print "Here are the months: ", months

print """ 
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" # whatever I write within the triple doube quotes gets printed verbatim. If I need to go to the next line I just have to type in the next line. This is good stuff. I can't even write a comment inside the """ thing.
