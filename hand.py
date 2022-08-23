import random
import console_display

def play_hand(hands, cards_per_hand, deck):
    shuffle_deck(deck)
    deal_cards(hands, cards_per_hand, deck)
    determine_pairs_in_hands(hands)
    console_display.display_all_hands(hands)
    winners = determine_hand_winners(hands)
    console_display.display_all_winners(winners)

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(hands, cards_per_hand, card_deck):
    for _ in range(cards_per_hand):
        for hand in hands:
            hand['cards'].append(card_deck.pop())

def determine_pairs_in_hands(hands):
    for index, hand in enumerate(hands):
        unique_cards = list(set(hand['cards']))
        if len(unique_cards) == len(hand['cards']):
            continue
        for card in unique_cards:
            if len([index for index, card_from_hand in enumerate(hand['cards']) if card_from_hand == card])  > 1:
                hands[index]['pairs'] += 1

def determine_hand_winners(hands):
    winning_number_of_pairs = find_max_pairs(hands)
    if winning_number_of_pairs == 0:
        return []
    return [hand for hand in hands if hand['pairs'] == winning_number_of_pairs]

def find_max_pairs(hands):
    max_pairs = 0
    for hand in hands:
        if hand['pairs'] > max_pairs:
            max_pairs = hand ['pairs']
    return max_pairs