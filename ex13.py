from sys import argv

script, first, second, third = argv
feeling = raw_input("How are you doing today? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "I'm feeling %s today." % feeling
