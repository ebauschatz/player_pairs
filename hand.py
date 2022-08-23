import random
import console_display

def play_hand(hands, cards_per_hand, deck):
    '''Play a single round of pairs and determine any winners
    Parameters:
        hands -- a list containing dictionary objects representing all hands in play
        cards_per_hands -- int representing the total number of cards that should be dealt to each hand
        deck -- list of all available cards not currently in a hand
    Effects:
        Cards are removed from the deck and added to the "cards" attribute of each hand
        The "wins" attribute is incremented for each hand determined to meet the win condition
    '''
    shuffle_deck(deck)
    deal_cards(hands, cards_per_hand, deck)
    determine_pairs_in_hands(hands)
    console_display.display_all_hands(hands)
    winners = determine_hand_winners(hands)
    track_wins(winners)
    console_display.display_hand_winners(winners)

# TODO: Create a function that shuffles without using random.shuffle
# Only using randint function
def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(hands, cards_per_hand, card_deck):
    for _ in range(cards_per_hand):
        for hand in hands:
            hand['cards'].append(card_deck.pop())

def determine_pairs_in_hands(hands):
    for index, hand in enumerate(hands):
        # TODO: Look up Lambda functions, the "filter" function, and use to find unique cards
        unique_cards = list(set(hand['cards']))
        if len(unique_cards) == len(hand['cards']):
            continue
        for card in unique_cards:
            if len([index for index, card_from_hand in enumerate(hand['cards']) if card_from_hand == card])  > 1:
                hands[index]['pairs'] += 1

def determine_hand_winners(hands):
    winning_number_of_pairs = find_max_value_from_key('pairs', hands)
    if winning_number_of_pairs == 0:
        return []
    return [hand for hand in hands if hand['pairs'] == winning_number_of_pairs]

def find_max_value_from_key(key, hands):
    current_max = 0
    for hand in hands:
        if hand[key] > current_max:
            current_max = hand[key]
    return current_max

def track_wins(winning_hands):
    for hand in winning_hands:
        hand['wins'] += 1