name = 'Emilie Lima Burke'
age = 23
height = 60  # inches
weight = 135  # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "She's %d inches (or %d centimeters) tall." % (height, height * 2.54)
print "She's %d pounds (or %d kilos) heavy." % (weight, weight / 2.2)
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are ususally %s depending on the coffee." % teeth

print "If I add %d, %d, and %d, I get %d." % (
	age, height, weight, age + height + weight)
