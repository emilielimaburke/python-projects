def debt_snowflakes(name, min_pay, balance):
	payments = (balance/min_pay) + 2
	print("You have %d payments left if you just pay the minimum." % payments)

	payments = (balance/(min_pay + 100)) + 2
	print("If you pay an extra $100 per month, your payments will go down to %d." % payments)

debt_count = int(raw_input("How many debts do you have? \n> "))

debts = range(debt_count + 1)
drop = debts.pop(0)

for debt in debts:
	if debt == 1:
		print("We're going to focus on just debt number %d" % debt)
	else:
		print("Now we're going to focus on debt number %d" % debt)

	name = raw_input("Who is your loan provider? \n> ")
	min_pay = float(raw_input("What is your minimum payment? \n> "))
	balance = float(raw_input("What is your current balance? \n> "))
	debt_snowflakes(name, min_pay, balance)

