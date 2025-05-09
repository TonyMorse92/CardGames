from card import Card
import itertools

class Deck:
	def make_deck(self):
		suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
		ranks = [str(i) for i in range (2,11)]
		ranks += ['Jack','Queen','King','Ace']
		return [Card(suit, rank) for suit in suits for rank in ranks]


deck = Deck().make_deck()

for card in deck:
	print(card.name)
