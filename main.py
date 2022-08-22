import random
import console_display
import game_settings

def main():
    cards_per_hand = game_settings.get_cards_per_hand()
    card_types = game_settings.get_card_types()
    number_of_each_type_in_deck = game_settings.get_number_of_each_type_in_deck()
    number_of_players = game_settings.get_number_of_players()
    console_display.display_welcome_message(cards_per_hand)
    deck = generate_deck(number_of_each_type_in_deck, card_types)
    shuffle_deck(deck)
    all_hands = generate_player_hands(number_of_players)
    deal_cards(all_hands, cards_per_hand, deck)
    determine_pairs_in_hands(all_hands)
    console_display.display_all_hands(all_hands)
    winners = determine_hand_winners(all_hands)
    console_display.display_all_winners(winners)

def generate_deck(type_repetitions, types):
    new_deck = []
    new_deck.extend(types * type_repetitions)
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

main()