i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print " Numbers now: ", numbers
    print "at the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

### Study Q 1 & 2
def counting(i, y):
    numbers = []
    while i < y:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print " Numbers now: ", numbers
        print "at the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

counting(0, 6)

##Study Q 3 & 4
def counting(i, y, m):
    numbers = []
    while i < y:
        print "At the top i is %d" % i
        numbers.append(i)

        i += m
        print " Numbers now: ", numbers
        print "at the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

counting(0, 6, 4)


## STudy Q 5

def counting(i, y, m):
    numbers = range(i,y)
    for num in numbers:
        print "The number is now: ", num

    print "The numbers: "

    for num in numbers:
        print num

counting(0, 6, 1)
