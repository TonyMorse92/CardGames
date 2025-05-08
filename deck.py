from card import Card

class Deck:
	def __init__(self):
		self.suit = suit

	def make_deck(self):
		if self.rank == 'Ace':
			return 11
		elif self.rank == 'King':
			return 10
		elif self.rank == 'Queen':
			return 10
		elif self.rank == 'Jack':
			return 10
		else:
			return int(self.rank)


print("hi")
