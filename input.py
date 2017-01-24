answer = input("Do you want to hear a joke? ")

yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]

if answer in yes:
	print("I'm against picketing, but I don't know how to show it." )
elif answer in no:
	print("Fine.")
else:
	print("I don't understand.")

