import random
import math

songs = [
	"Time (Alan Walker Remix)",
	"Man On The Moon",
	"Alone, Pt. II",
	"Paradise",
	"Out Of Love",
	"Red Nexus Rising (Interlude)"
]

class entry:
	def __init__(self, name, rating, rd):
		self.name = name
		self.rating = rating
		self.rd = rd
		self.score = 0

class combination:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.outcome = 0.5

	def as_string(self):
		return self.player1.name + " vs. " + self.player2.name

entries = list(map(lambda name: entry(name, 1500, 350), songs))

combinations = []

for x in range(0, len(entries)):
	for y in range (x + 1, len(entries)):
		combinations.append(combination(entries[x], entries[y]))

random.shuffle(combinations)

print("World of Walker songs rank computer")
print("Enter 1 to choose the first option")
print("Enter 2 to choose the second option")
print("Entering anything else will draw the choice")
print()

for x in combinations:
	print("1) " + x.player1.name)
	print("2) " + x.player2.name)
	choice = input("Enter your choice: ")
	if (choice == "1"):
		x.player1.score += 1
		x.player2.score -= 1
	elif (choice == "2"):
		x.player1.score -= 1
		x.player2.score += 1

new_entries = []

for e in entries:
	entry_things = list(filter(lambda c: c.player1 == e or c.player2 == e, combinations))
	new_r = e.rating + e.score * 400 / len(entry_things)
	new_entries.append(entry(e.name, new_r, e.rd))

new_entries.sort(key=lambda x: x.rating, reverse=True)
print()
for x in new_entries:
	print(x.name + " " + str(x.rating))
