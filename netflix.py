# What Should I Watch Tonight?

import random

#Potential Shows
shows = ["One Tree Hill", 
         "Sons of Anarchy", 
         "Gilmore Girls", 
         "The Man in the High Castle",
         "The West Wing"]

#Potential Locations
places = ["couch",
          "recliner",
          "loveseat",
          "bed",
          "floor"]

random_show = random.choice(shows)
random_place = random.choice(places)


print("I think I will watch %s from %s tonight." % (random_show, random_place))