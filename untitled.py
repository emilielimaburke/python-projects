class Meal():

	def __init__(self,protein, carb, fat):
		self.protein = protein
		self.carb = carb
		self.fat = fat

	def macro_breakdown(protein, carb, fat):
		return "%dP, %dC, %dF"

yest_bfast = Meal(10, 28, 8)

print yest_bfast.macro_breakdown()