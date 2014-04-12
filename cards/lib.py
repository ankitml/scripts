#library for basic card functions
# a card is defined as '23456789TJQKA' + 'SCHD'
# AC, JD, 2H etc etc

def deal(players, cards = 5, deck=None, format='list'):
	""" 
	deals out cards to n players with cards number of cards.
	Number of cards default will be 5
	default value of deck will be a new single deck. 
	"""

	if not deck:
		deck = [card + suite 
				for card in '23456789TJQKA' 
				for suite in 'SCHD']
	import random
	random.shuffle(deck)
	hands = []
	for i in range(0,players):
		hand = deck[i * cards : (i + 1) * cards ]
		if format == 'string' :
			hands.append(' '.join(hand))
		if format == 'list' :
			hands.append(hand)
	return hands

def card_rank(card):
	"""
	return rank of a single card
	card is given as a string 'AH' or '2C' 
	"""
	return '--23456789TJQKA'.index(card[0])

def hand_rank(hand):
	"""
	returns rank of the hand
	hand is given as a list of cards (not string)
	"""
	return card_rank(max(hand, key=card_rank))


def tests():
	return 0