# define variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)  # 1

# print variables
print x
print y

# print with more fanciness
print "I said: %r." % x  # 2
print "I also said: '%s'." % y  # 3

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"  # 4

# hilarious becomes the variable being called by the '%r' in the variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# concatenation when plus is used on two strings
print w + e
