import random
import sys
from card import Card
from player import Player

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = [str(i) for i in range (2,11)]
ranks += ['Jack','Queen','King','Ace']


deck = [Card(suit,face) for suit in suits for face in ranks]

print(f'First card: {deck[0].name}')

# Shuffle 3 times. No cheating here
random.shuffle(deck)
random.shuffle(deck)
random.shuffle(deck)

print(f'First card after shuffling: {deck[0].name}')

dealer = Player()
me = Player()
me.draw(deck, 2)
dealer.draw(deck,2)
dealer.update_score()
me.update_score()
print(f'First score: {me.get_score()}')
print(f'First hand: {me.get_hand()}')
print(f'Pretend dealer hand: {dealer.get_dealer_hand()}')


action = ''


# Need to check if Player has a 21. If they do, they win
action = 'H'
	
while action == 'H':
	action = input("Do you want to [H]it or [S]tay?")

	if action == 'H':
		me.draw(deck,1)
		# TODO: Maybe it makes more sense for get_score to update the score automatically?
		me.update_score() 
		if me.get_score() == 21:
			print("YOU WIN!!!")
			sys.exit()
		elif me.get_score() > 21:
			print("YOU LOSE!!!")
			sys.exit()
		print(f'Score: {me.get_score()}')
		print(f'Hand: {me.get_hand()}')
		print(f'Pretend dealer hand: {dealer.get_dealer_hand()}')

		# Then needs to ask again
		# If the player busts, no need to do anything with the dealer, player loses
	elif action == 'S':
		pass
		# This will be the Dealer's logic to see if they stay or hit
		# If the Dealer would stay (so they are winning), can just reveal all the cards and say player wins
	else:
		print("Enter an H for hit or S for stay")
		# Loop again
