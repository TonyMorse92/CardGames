class Player:
	def __init__(self):
		self.score = 0
		self.hand = []

	def initial_draw(self,Deck):
		print(f'First card in player class deck: {Deck[0].name}')
		print(f'hand before append:  {self.hand}')
		self.hand.append(Deck[0])
		self.hand.append(Deck[1])
		print(f'hand after append: {self.hand}')
		print(f'Player hand: {self.hand[0].name}  and  {self.hand[1].name}')
		del Deck[0]
		del Deck[1]

	def draw(self, Deck, num_cards_to_draw):
		cards_drawn = 0
		while(cards_drawn < num_cards_to_draw):
			self.hand.append(Deck[0])
			del Deck[0]
			cards_drawn += 1

	def get_hand(self, is_dealer=False):
		hand = [card.name for card in self.hand]
		# Dealer doesn't show one card
		if is_dealer:
			return hand[1:]
		else:
			return hand	

	def get_score(self):
		return self.score

	def update_score(self):
		self.score = sum([card.get_card_val() for card in self.hand]) 

# Dealer shows all but the first card
# It would probably make sense for Dealer to be a subclass of player
# with special methods for hiding cards.
# Or maybe a sepearte class, since it will be a computer with its own play logic
	def get_dealer_hand(self):
		hand = [card.name for card in self.hand]
		hand.pop(0)
		return hand
