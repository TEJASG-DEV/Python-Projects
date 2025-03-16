# A BlackJack game implementation kind of casino style ;-)
import random # To choose cards in random and to shuffle the cards ofcourse
import os

# Let's keep a track of the card's values
card_values = {2:2,
			   3:3,
			   4:4,
			   5:5,
			   6:6,
			   7:7,
			   8:8,
			   9:9,
			   10:10,
			   'K':10,
			   'Q':10,
			   'J':10}

# The Ace seems missing... This is on purpose... Because Ace can be 1 or 11 based on the situation.

# Now let's make a score calculator. I have tested almost all corner cases as per rules using this URL:
# https://wizardofodds.com/games/blackjack/hand-calculator/
def calc_score(card_list):
	total_score = 0
	for card in card_list: # Calculate the sum of Non Ace cards this makes calculating score a TON easier
		if not (card == 'A'):
			total_score += card_values[card]
		else:
			pass
	
	ace_score = 0
	ace_count = 0 # Just in case soft total exceeds 21

	for card in card_list:
		if card == 'A' and total_score < 11 and total_score < 21: # This total is the hard total result from above loop.
			ace_count += 1
			total_score += 11
			ace_score += 11 # updates ace_score by the same
		elif card == 'A' and total_score >= 11 and total_score < 21: # This shit... the comparision with  21 is important.
			ace_count += 1 # If score goes above 21 because of aces, then the soft score of 11 has to be removed...
			total_score += 1
			ace_score += 1 # updates ace_score by the same... keeping track of total aces added
		elif card == 'A' and total_score >= 21:
			ace_count += 1
			total_score -= ace_score # undo all the addition done before. as the aces must have values = 1
			total_score += ace_count 
			
	return total_score

# Now for the draw function which draws the first n cards from the pre shuffled deck of 52 cards and appends it to given list.
def draw(card_list_to_be_appended, num_times):
	for i in range(0, num_times):
		card_list_to_be_appended.append(cards.pop(0))
# The above can be used to draw cards out in random... using the pop() function of lists.

# A Win or lose calculator based on the rules.
def win_or_lose(player_cards, dealer_cards):
	player_score = calc_score(player_cards)
	dealer_score = calc_score(dealer_cards)
	if player_score > 21 and dealer_score <= 21: # The first case may never occur because code in the while (see if statement)
		print("You Bust. You lose.") # But this redundant code is still useful anyways.
	elif dealer_score > 21 and player_score <= 21:
		print("Dealer Busts. You win.")
	elif player_score == 21 and player_score > dealer_score:
		print("You win with a blackjack.")
	elif dealer_score == 21 and dealer_score > player_score:
		print("Dealer wins with a blackjack. You lose.")
	elif dealer_score == player_score:
		print("It's a draw!")
	elif player_score > dealer_score:
		print("You win with a greater score.")
	elif dealer_score > player_score:
		print("Dealer wins with a greater score. You lose.")
	else:
		print("Some corner case. Make rules for that.")
	
# The logo part:
logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \\/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      '------'                           |__/           
'''

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if choice == 'y':
	os.system('clear')
	print(logo)
	want_to_play = True
elif choice == 'n':
	want_to_play = False
else: 
	print("Man, just type 'y' or 'n'. It's that simple.")
	want_to_play = False
# Now for the game part:
initial_draw = False

player_cards = []
dealer_cards = []

while want_to_play:

	if initial_draw == False:
		# Let's have a deck of 52 cards
		cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'K','K','K','K','Q','Q','Q','Q','J','J','J','J','A','A','A','A']
		# For the sake of lesser bugs
		player_cards = []
		dealer_cards = []
		# Shuffle the deck randomly
		random.shuffle(cards) # Once shuffled, cards drawn are random.
		# Draw 2 cards in random for the player and the dealer.
		draw(player_cards, 2)
		draw(dealer_cards, 2)
		initial_draw = True
	
	print(f"Your cards: {player_cards}, current score = {calc_score(player_cards)}")
	print(f"Dealer's First card: {dealer_cards[0]}")
	
	take_more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
	
	if take_more_cards == 'y':
		draw(player_cards, 1)
		player_score = calc_score(player_cards)
		dealer_score = calc_score(dealer_cards)
		if player_score > 21 and dealer_score <= 21:
			print(f"Your cards: {player_cards}, current score = {calc_score(player_cards)}")
			print(f"Dealer's First card: {dealer_cards[0]}")

			print(f"Your final hand: {player_cards}, final score: {player_score}")
			print(f"Dealer's final hand = {dealer_cards}, dealer's final score: {dealer_score}")
			print("You Bust. You Lose.")
			
			choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
			if choice == 'y':
				want_to_play = True
				initial_draw = False
				os.system('clear')
				print(logo)
			elif choice == 'n':
				want_to_play = False
				initial_draw = False
			else:
				print("Man, just type 'y' or 'n'. It's that simple.")
				wan_to_play = False
				initial_draw = False
		else:
			#print(f"Passed the if within take_more_cards if statement.")
			pass
	elif take_more_cards == 'n':
		while calc_score(dealer_cards) < 17:
			draw(dealer_cards, 1)
		print(f"Your final hand: {player_cards}, your final score: {calc_score(player_cards)}")
		print(f"Dealer's final hand = {dealer_cards}, dealer's final score: {calc_score(dealer_cards)}")
		win_or_lose(player_cards, dealer_cards)
		
		choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
		if choice == 'y':
			want_to_play = True
			initial_draw = False
			os.system('clear')
			print(logo)
		elif choice == 'n':
			want_to_play = False
			initial_draw = False
		else:
			print("Man, just type 'y' or 'n'. It's that simple.")
			wan_to_play = False
			initial_draw = False
