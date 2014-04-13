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

def card_ranks(hand):
	return [card_rank(card) for card in hand]

def hand_rank(hand):
	"""
	returns rank of the hand
	hand is given as a list of cards (not string)
	is this even useful?
	"""
	return card_rank(max(hand, key=card_rank))

def kind(n, hand):
	"""
	is the given hand n of a kind.
	returns true or false
	"""

def straight(hand):
	"""
	is the hand straight
	"""
	ranks = card_ranks(hand)
	if (max(ranks) - min(ranks) == 4) and (len(set(ranks)) == 5):
		return True
	else:
		return False

def flush(hand):
	"""
	is the hand a flush
	"""
	suite = hand[1][1]
	for card in hand:
		if card[1] != suite:
			return False
	return True


def full_house(hand):
	"""
	is this full house
	three of a kind and 2 of a kind
	"""
	if kind(2, hand) and kind(3,hand) :
		return True
	else:
		return False

def two_pair(hand):
	"""
	is the hand two pair
	"""
	ranks = card_ranks(hand)
	ranks.sort()
	


def poker_rank(hand):
	"""
	ranks the hand on basis of poker rules
	straight flush is ranked 8
	four of a kind is ranked 7
	full house is ranked 6
	flush is ranked 5
	straight is ranked 4
	three of a kind is ranked 3
	two pair is ranked 2
	pair is ranked 1
	high card  is ranked 0
	"""
	if straight(hand) and flush(hand):
		return 8
	if kind(4,hand):
		return 7
	if full_house(hand):
		return 6
	if flush(hand):
		return 5
	if straight(hand):
		return 4
	if kind(3, hand):
		return 3
	if two_pair(hand):
		return 2
	if kind(2, hand):
		return 1
	else:
		return 0



def tests():
	return 0