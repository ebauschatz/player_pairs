import console_display
import game_settings
from hand import play_hand

def main():
    cards_per_hand, card_types, number_of_each_type_in_deck, number_of_players = initial_game_settings()
    console_display.display_welcome_message(cards_per_hand)
    deck, all_hands = game_setup(number_of_players, card_types, number_of_each_type_in_deck)
    play_hand(all_hands, cards_per_hand, deck)

def initial_game_settings():
    cards_per_hand = game_settings.get_cards_per_hand()
    card_types = game_settings.get_card_types()
    number_of_each_type_in_deck = game_settings.get_number_of_each_type_in_deck()
    number_of_players = game_settings.get_number_of_players()
    return cards_per_hand, card_types, number_of_each_type_in_deck, number_of_players

def game_setup(number_of_players, card_types, number_of_each_type_in_deck):
    deck = generate_deck(number_of_each_type_in_deck, card_types)
    all_hands = generate_player_hands(number_of_players)
    return deck, all_hands

def generate_deck(type_repetitions, types):
    new_deck = []
    new_deck.extend(types * type_repetitions)
    return new_deck

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


main()