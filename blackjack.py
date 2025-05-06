import random
import sys
from card import Card
from player import Player

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = [str(i) for i in range (2,11)]
ranks += ['Jack','Queen','King','Ace']

## TODO: Deck should probably be its own class if I'm doing it like this.
deck = [Card(suit,face) for suit in suits for face in ranks]

# Shuffle 3 tiplayers. No cheating here
random.shuffle(deck)
random.shuffle(deck)
random.shuffle(deck)

dealer = Player()
player = Player()
player.draw(deck, 2)
dealer.draw(deck,2)
dealer.update_score()
player.update_score()
print(f'Hand: {player.get_hand()}')
print(f'Dealer hand: {dealer.get_hand(hide_hand=True)}')


# Need to check if Player has a 21. If they do, they win
action = 'H'
	
while action == 'H':
	action = input("\nDo you want to [H]it or [S]tay?\n")

	if action == 'H':
		player.draw(deck,1)
		# TODO: Maybe it makes more sense for get_score to update the score automatically?
		player.update_score() 
		if player.get_score() == 21:
			print(f'Hand: {player.get_hand()}')
			print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
			print("YOU WIN!!!")
			sys.exit()
		elif player.get_score() > 21:
			print(f'Hand: {player.get_hand()}')
			print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
			print("YOU LOSE!!!")
			sys.exit()
		print(f'Hand: {player.get_hand()}')
		print(f'Dealer hand: {dealer.get_hand(hide_hand=True)}')

		# Then needs to ask again
		# If the player busts, no need to do anything with the dealer, player loses
	elif action == 'S':
		if dealer.get_score() < player.get_score():
			dealer.draw(deck,1)
			dealer.update_score()
			if dealer.get_score() > 21:
				print(f'YOU WIN!!!!')	
				print(f'Hand: {player.get_hand()}')
				print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
			else:
				if(player.get_score() >= dealer.get_score()):
					print(f'YOU WIN!!!!')	
					print(f'Hand: {player.get_hand()}')
					print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
				
		
		else:
			print(f'Hand: {player.get_hand()}')
			print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
			print(f'YOU LOSE!!!')

		# This will be the Dealer's logic to see if they stay or hit
		# If the Dealer would stay (so they are winning), can just reveal all the cards and say player wins
	else:
		print("\nEnter an H for hit or S for stay")
		# Loop again
