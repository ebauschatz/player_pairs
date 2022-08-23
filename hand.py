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

def shuffle_deck(deck):
    for card_indexes_remaining_to_shuffle in range(len(deck) - 1, -1, -1):
        index_of_card = random.randint(0, card_indexes_remaining_to_shuffle)
        deck.append(deck.pop(index_of_card))

def deal_cards(hands, cards_per_hand, card_deck):
    for _ in range(cards_per_hand):
        for hand in hands:
            hand['cards'].append(card_deck.pop())

def determine_pairs_in_hands(hands):
    for index, hand in enumerate(hands):
        # TODO: Look up Lambda functions, the "filter" function, and use to find unique cards
        all_cards = hand['cards']
        unique_cards_and_positions = list(filter(lambda card: card[1] not in all_cards[card[0] + 1:], enumerate(all_cards)))
        if len(unique_cards_and_positions) == len(all_cards):
            continue
        for _, card in unique_cards_and_positions:
            if all_cards.count(card) > 1:
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