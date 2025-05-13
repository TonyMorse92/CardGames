class Player:
	def __init__(self):
		self.score = 0
		self.hand = []

	def draw(self, deck, num_cards):
		cards_drawn = 0
		while(cards_drawn < num_cards):
			self.hand.append(deck[0])
			del deck[0]
			cards_drawn += 1

	def get_hand(self, hide_hand=False):
		hand = [card.name for card in self.hand]
		# Dealer doesn't show one card
		if hide_hand:
			return hand[1:]
		else:
			return hand	

	def get_score(self):
		return self.score

	def update_score(self):
		self.score = sum([card.get_card_val() for card in self.hand]) 
