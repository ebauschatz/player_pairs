import console_display
from game import initial_game_settings, game_setup, play_game

def main():
    cards_per_hand, card_types, number_of_each_type_in_deck, number_of_players, number_of_rounds = initial_game_settings()
    console_display.display_welcome_message(cards_per_hand)
    deck, all_hands = game_setup(number_of_players, card_types, number_of_each_type_in_deck)
    play_game(all_hands, cards_per_hand, deck, number_of_rounds)


main()