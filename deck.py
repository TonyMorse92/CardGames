from card import Card

class Deck:
	def make_deck(self):
		suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
		ranks = [str(i) for i in range (2,11)]
		ranks += ['Jack','Queen','King','Ace']
		return [Card(suit, rank) for suit in suits for rank in ranks]

