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

# Need to check if Player has a 21. If they do, they win
action = input("\nDo you want to [H]it or [S]tay?\n")

while action == 'H':

player.draw(deck,1)
player.update_score() 


if player.get_score() > 21:
print(f'Hand: {player.get_hand()}')
print('Bust. You lose!')
quit()


elif player.get_score() == 21:
print(f'Hand: {player.get_hand()}')
print("21. You win!")
quit()


action = input("\nDo you want to [H]it or [S]tay?\n")
print("YOU LOSE!!!")
quit()
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
if dealer.get_score() < player.get_score():
dealer.draw(deck,1)
dealer.update_score()
if dealer.get_score() > 21:
print(f'YOU WIN!!!!')	
print(f'Hand: {player.get_hand()}')
print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
elif player.get_score() >= dealer.get_score():
print(f'YOU WIN!!!!')	
print(f'Hand: {player.get_hand()}')
print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
else:
if(player.get_score() >= dealer.get_score()):
	print(f'YOU WIN!!!!')	
	print(f'Hand: {player.get_hand()}')		
else:
	print(f'Hand: {player.get_hand()}')
	print(f'Dealer hand: {dealer.get_hand(hide_hand=False)}\n')
print(f'YOU LOSE!!!')
