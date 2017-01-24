def print_two(name,age):
	print("Your name is %s" % name)
	print("Your age is %d" % age)

def print_one(name):
	print("Your name is: %s" % name)

def print_none():
	print("I got nothin'")

#print_two("Emilie", 23)
#print_one("Emilie")
#print_none()

def add(a, b):
	print("adding %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("subtracting %d - %d" % (a,b))
	return a - b

def multiply(a,b):
	print("multiplying %d * %d" % (a,b))
	return a * b

def divide(a,b):
	print("dividing %d/%d" % (a,b))
	return a/b

age = add(float(input("Write 20 ")),float(input("Write 3 ")))
weight = multiply(44,3)
height = subtract(70,10)
iq = divide(140,2)

print("Age: %d, Height: %d, Weigh: %d, IQ: %d" % (age, height, weight, iq))

def reverse_and_upper(apple):
	return apple.upper()[::-1]

print(reverse_and_upper('#BotheAmericanBulldog'))
