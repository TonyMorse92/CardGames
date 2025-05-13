import random
import sys
import time
from card import Card
from player import Player
from deck import Deck

deck = Deck().make_deck()
random.shuffle(deck)


computer = Player()
player = Player()

player.draw(deck, 2)
computer.draw(deck,2)

computer.update_score()
player.update_score()

#TODO: Eventually make this check if they want to play again.
def quit():
	sys.exit()

print(f'Hand: {player.get_hand()}')
print(f'Computer hand: {computer.get_hand(hide_hand=True)}')


# Begin Game Loop
action = input("\nDo you want to [H]it or [S]tay?\n")

while action == 'H':
	player.draw(deck,1)
	player.update_score() 
	print(f'\nHand: {player.get_hand()}')
	print(f'Computer hand: {computer.get_hand(hide_hand=True)}')

	if player.get_score() > 21:
		print('Bust. You lose!')
		quit()
	elif player.get_score() == 21:
		print("21. You win!")
		quit()
	else:
		action = input("\nDo you want to [H]it or [S]tay?\n")


# Player has finished drawing. Computer's turn. I think that's how Blackjack works? 
# At this point, the Player hasn't gone over 21, and the computer can't have either
# Ties go to the player, I think. Can separate that out later, for now, just have computer
# draw again and bust
while computer.get_score() <= player.get_score():
	print(f'\nHand: {player.get_hand()}')
	print(f'Computer hand: {computer.get_hand(hide_hand=False)}\n')	
	computer.draw(deck,1)
	computer.update_score()

	# Give the player some time to process what happened.
	# Parameter is number of seconds to wait.
	time.sleep(1.5)

	if computer.get_score() > 21:
		print(f'\nHand: {player.get_hand()}')
		print(f'Computer hand: {computer.get_hand(hide_hand=False)}\n')
		print(f'Computer bust. You win!')	
		quit()


# Only way we haven't exited yet is if computer has higher hand and didn't bust
print(f'\nHand: {player.get_hand()}')
print(f'Computer hand: {computer.get_hand(hide_hand=False)}\n')
print(f'Computer higher. You lose!')	
quit()
