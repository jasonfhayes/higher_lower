import random
import os

# Main game loop:
while True:

	# Welcome the player
	print('Welcome to the game Higher or Lower!')
	print()
	
	# Set up some basic stuff:
	number_to_draw = 8
	rank_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	suit_list = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	drawn_cards = []
	counter = 0
	user_score = 0
	
	# Draw a set of cards to play with:
	for i in range(number_to_draw):
		while True:
			data_pair = (random.choice(rank_list), random.choice(suit_list))
			if data_pair not in drawn_cards:
				drawn_cards.append(data_pair)
				break
	
	# Begin individual round loop:
	for i in range(len(drawn_cards) - 1):

		current_card = drawn_cards[counter]
		next_up = drawn_cards[counter+1]
		
		print(f'Round {counter + 1}:')
		
		if current_card[0] == 11:
			print(f'Current card is the Jack of {current_card[1]}.')
		elif current_card[0] == 12:
			print(f'Current card is the Queen of {current_card[1]}.')
		elif current_card[0] == 13:
			print(f'Current card is the King of {current_card[1]}.')
		elif current_card[0] == 14:
			print(f'Current card is the Ace of {current_card[1]}.')
		else:	
			print(f'Current card is the {current_card[0]} of {current_card[1]}.')
		
		while True:	
			user_input = input('Do you think the next card is higher or lower? Type "H" or "L": ')
			user_input = user_input.upper()
			if 'H' in user_input or 'L' in user_input:
				break
			else:
				print('Please type "H" or "L"')
		
		if user_input == 'H' or user_input == 'h':
			user_input = 'h'
		else:
			user_input = 'l'

		# Begin Card Evaluation Logic Code
		# Compare different ranked cards:
		if current_card[0] > next_up[0]:
			next_card = 'l'
		if current_card[0] < next_up[0]:
			next_card = 'h'
		# Compare equal ranked cards by suit:
		if current_card[0] == next_up[0] and current_card[1] == 'Clubs':
			next_card = 'h'
		if current_card[0] == next_up[0] and current_card[1] == 'Spades':
			next_card = 'l'
		if current_card[0] == next_up[0] and current_card[1] == 'Hearts' and next_up[1] == 'Spades':
			next_card = 'h'
		if current_card[0] == next_up[0] and current_card[1] == 'Hearts' and next_up[1] != 'Spades':
			next_card = 'l'
		if current_card[0] == next_up[0] and current_card[1] == 'Diamonds' and next_up[1] == 'Clubs':
			next_card = 'l'
		if current_card[0] == next_up[0] and current_card[1] == 'Diamonds' and next_up[1] != 'Clubs':
			next_card = 'h'
		# End Card Evaluation Logic Code
		
		# Special print statements to use words like "Jack" "Queen" "King" and "Ace":
		# Jacks:
		if next_up[0] == 11 and user_input == next_card:
			print('Correct. +10 Points')
			print(f'Next card was the Jack of {next_up[1]}')
			user_score += 10
			print(f'Current score: {user_score}')
			print()
		if next_up[0] == 11 and user_input != next_card:
			print('Incorrect. -5 Points')
			print(f'Next card was the Jack of {next_up[1]}')
			user_score -= 5
			print(f'Current score: {user_score}')
			print()
			
		# Queens:
		if next_up[0] == 12 and user_input == next_card:
			print('Correct. +10 Points')
			print(f'Next card was the Queen of {next_up[1]}')
			user_score += 10
			print(f'Current score: {user_score}')
			print()
		if next_up[0] == 12 and user_input != next_card:
			print('Incorrect. -5 Points')
			print(f'Next card was the Queen of {next_up[1]}')
			user_score -= 5
			print(f'Current score: {user_score}')
			print()
			
		# Kings:
		if next_up[0] == 13 and user_input == next_card:
			print('Correct. +10 Points')
			print(f'Next card was the King of {next_up[1]}')
			user_score += 10
			print(f'Current score: {user_score}')
			print()
		if next_up[0] == 13 and user_input != next_card:
			print('Incorrect. -5 Points')
			print(f'Next card was the King of {next_up[1]}')
			user_score -= 5
			print(f'Current score: {user_score}')
			print()
		
		# Aces:
		if next_up[0] == 14 and user_input == next_card:
			print('Correct. +10 Points')
			print(f'Next card was the Ace of {next_up[1]}')
			user_score += 10
			print(f'Current score: {user_score}')
			print()
		if next_up[0] == 14 and user_input != next_card:
			print('Incorrect. -5 Points')
			print(f'Next card was the Ace of {next_up[1]}')
			user_score -= 5
			print(f'Current score: {user_score}')
			print()
			
		# Regular print statemnts for cards ranked 2 - 10:
		if user_input == next_card and next_up[0] < 11:
			print('Correct. +10 Points')
			print(f'Next card was the {next_up[0]} of {next_up[1]}')
			user_score += 10
			print(f'Current score: {user_score}')
			print()
		if user_input != next_card and next_up[0] < 11:
			print('Incorrect. -5 Points')
			print(f'Next card was the {next_up[0]} of {next_up[1]}')
			user_score -= 5
			print(f'Current score: {user_score}')
			print()
		
		counter += 1
	
	# End game messages:
	print('Thanks for playing.')
	print(f'Final score: {user_score}')
	print()
	
	# Ask to play again:
	while True:	
		play_again = input('Play again? Y or N: ')
		play_again = play_again.upper()
		if 'Y' in play_again or 'N' in play_again:
			break
		else:
			print('Please type "Y" or "N"')

	if play_again == 'Y':
		os.system("clear")
	else:
		print()
		print('Goodbye.')
		break