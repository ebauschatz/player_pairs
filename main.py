import enum
import random
import console_display

def main():
    cards_per_hand = 5
    number_of_each_type_in_deck = 4
    number_of_players = 4
    console_display.display_welcome_message(cards_per_hand)
    deck = generate_deck(number_of_each_type_in_deck)
    shuffle_deck(deck)
    all_hands = generate_player_hands(number_of_players)
    deal_cards(all_hands, cards_per_hand, deck)
    determine_pairs_in_hands(all_hands)
    console_display.display_all_hands(all_hands)
    #determine and display the winner(s)

def generate_deck(type_repetitions):
    card_types = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    new_deck = []
    new_deck.extend(card_types * type_repetitions)
    return new_deck

def shuffle_deck(deck):
    random.shuffle(deck)

def generate_player_hands(number_of_hands):
    new_hands = []
    for hand_number in range(number_of_hands):
        hand = {
            'name': get_hand_name(hand_number),
            'cards': [],
            'pairs': 0
        }
        new_hands.append(hand)
    return new_hands

def get_hand_name(hand_number):
    return f'Player {hand_number + 1}'

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


main()