import random
import sys
from card import Card
from player import Player
from deck import Deck

deck = Deck().make_deck()
random.shuffle(deck)


dealer = Player()
player = Player()

player.draw(deck, 2)
dealer.draw(deck,2)

dealer.update_score()
player.update_score()

#TODO: Eventually make this check if they want to play again.
def quit():
	sys.exit()

print(f'Dealer hand: {dealer.get_hand(hide_hand=True)}')
print(f'Hand: {player.get_hand()}')


# Begin Game Loop
action = input("\nDo you want to [H]it or [S]tay?\n")

while action == 'H':
	player.draw(deck,1)
	player.update_score() 
	print(f'\nHand: {player.get_hand()}')

	if player.get_score() > 21:
		print('Bust. You lose!')
		quit()
	elif player.get_score() == 21:
		print("21. You win!")
		quit()
	else:
		action = input("\nDo you want to [H]it or [S]tay?\n")


# Player has finished drawing. Dealer's turn. I think that's how Blackjack works? 
# At this point, the Player hasn't gone over 21, and the dealer can't have either
# Ties go to the player, I think. Can separate that out later, for now, just have dealer
# draw again and bust
while dealer.get_score() <= player.get_score():
	print(f'\nHand: {player.get_hand()}')
	print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')	
	dealer.draw(deck,1)
	dealer.update_score()
	if dealer.get_score() > 21:
		print(f'\nHand: {player.get_hand()}')
		print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
		print(f'Dealer bust. You win!')	
		quit()


# Only way we haven't exited yet is if dealer has higher hand and didn't bust
print(f'\nHand: {player.get_hand()}')
print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
print(f'Dealer higher. You lose!')	
quit()
