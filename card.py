class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.name = f'{rank} of {suit}s'

	def get_card_val(self):
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
