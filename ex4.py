cars = 100 # Assign the value 100 to a variable named cars
space_in_a_car = 4.0 # Assign the value 4.0 to another variable I think there is a floating point here because there might be a time in the future where we might have to make an adjusment for a baby. Babies might count as half a person.(=
drivers = 30 # And it continues
passengers = 90 # same thing
cars_not_driven = cars - drivers # subtracting two variables and storing it in a new variable. Each driver can drive only one car so the number of 'undriven' cars is the Total number of cars minus the total number of drives.
cars_driven = drivers # The preceeding point put in a different way. Literally using a different variables. I also noted one additional thing. The values of the stuff in the right is assigned to the stuff in left. Stuff includes variables, numbers and anyother thing that can hold values or even expressions
carpool_capacity = cars_driven * space_in_a_car # Expression evaluvated first and then the value of the expression is stored in the variable to the left.
average_passengers_per_car = passengers / cars_driven # same thing

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# I also noticed one more interesting thing now. 
