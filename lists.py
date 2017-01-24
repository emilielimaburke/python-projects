people = ["Emilie", "Laura", "Casey", "Kyle"]
ages = [23, 21, 23, 26]
things =["Bo", "Fluffy", False, 55]

print("These are the people I like: {}, {}, and {}".format(people[1], people[2], people[3]))


print("This is things:", things)

things.append("banana")
print("This is things now:", things)

sentence = "Emilie is really beautiful"
words = sentence.split()
print("The words are:", words)

things.append(people)
print("This is things now", things)
print("This is the first person in the last thing:", things[-1][0])