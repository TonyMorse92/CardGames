# TODO: Add UI and use pygame
# TODO: Allow users to switch between games.
import blackjack


action = input("Do you want to play blackjack?\n")

if action == "Y":
	blackjack.play()
