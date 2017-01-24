# What Should I Do Tonight?

import random

# Our list of bars
bars = ["Lion's Head Tavern",
        "The Hamilton",
        "1020 Bar",
        "Amsterdam Tavern",
        "The Heights",
        "The Dead Poet",
        "Prohibition"]

# Our list of friends
people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Alexander Hamilton",
          "Samuel L. Jackson",
          "Kanye West"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_second_person = random.choice(people)

print("How about you go to %s with %s and %s?" % (random_bar, random_person, random_second_person))
print("How about you go to {} with {} and {}?".format(random_bar, random_person, random_second_person))