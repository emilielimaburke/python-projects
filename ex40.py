class Song(object):

	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
				print line

happy_bday = Song(["Happy birthday to you",
				   "I hdon't want to get suite",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", 
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#### Pets http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/
# class Pet():

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def getName(self):
#         return self.name

#     def getSpecies(self):
#         return self.species

#     def __str__(self):
#         return "%s is a %s" % (self.name, self.species)

# my_dog = Pet("Bo", "Dog")
# print "Bo is a %s" % my_dog.getSpecies()
# print "Bo is a %s" % Pet.getSpecies(my_dog)

# print my_dog.getName()


#### MEAL
# class Meal():

# 	def __init__(self, protein, carb, fat):
# 		self.protein = protein
# 		self.carb = carb
# 		self.fat = fat

# 	def macro_breakdown(self):
# 		return "%dP, %dC, %dF" % (self.protein, self.carb, self.fat)

# yest_bfast = Meal(10, 28, 8)

# print "Yesterday's breakfast had %s." % yest_bfast.macro_breakdown()