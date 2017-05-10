# close - closes file
# read - reads the contents of the file; results can be assigned to a variable
# readline - reads just one line of text file
# truncate - empties the file
# write(stuff) - writes stuff to the file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') 
#We use a 'w' mode here so that we're maintaining the option of writing to the file.
#r is reading
#a is appending

print "Truncating the file. Goodbye!"
target.truncate()
#This is superfluous https://docs.python.org/2/library/functions.html#open

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s \n%s \n%s \n" % (line1, line2, line3))

print "And finally, we close it."
target.close()
