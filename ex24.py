print "Let's practice everything."
# Escape sequences here
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# input within """. we add multiple lines inside the """
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print '-' * 14
print poem
print '-' * 14

five = 10 - 2 + 3 - 6
print "This should be five: %s." % five

# function definiton here. Always end with :
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
# the variables are assigned in the order they are returned.
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point /= 10

print "We can also have it this way:"
# variables printed in the way they are returned.
print "We'd have %d beans, %d jars, %d crates." % secret_formula(start_point)
