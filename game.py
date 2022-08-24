import game_settings
import console_display
from hand import play_hand, find_max_value_from_key

def initial_game_settings():
    '''Gets values for configurable or hard-coded game settings and returns them all.'''
    cards_per_hand = game_settings.get_cards_per_hand()
    card_types = game_settings.get_card_types()
    number_of_each_type_in_deck = game_settings.get_number_of_each_type_in_deck()
    number_of_players = game_settings.get_number_of_players()
    number_of_rounds = game_settings.get_number_of_rounds()
    return cards_per_hand, card_types, number_of_each_type_in_deck, number_of_players, number_of_rounds

def game_setup(number_of_players, card_types, number_of_each_type_in_deck):
    '''Initializes the deck and all hands for the first round of play based on game settings.

    Parameters:
        number_of_players -- int representing the total number of hands to create
        card_types -- list of strings representing each type of card that should be included in the deck
        number_of_each_type_in_deck -- int representing the number of instances of each element of card_types in the final deck
    Returns:
        deck -- list of all available cards. each card is a string 
        all_hands -- list of dictionary objects representing all hands in play, with all attributes other than the name empty
    '''
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
            'pairs': 0,
            'wins': 0
        }
        new_hands.append(hand)
    return new_hands

def get_hand_name(hand_number):
    return f'Player {hand_number + 1}'

def play_game(all_hands, cards_per_hand, deck, number_of_rounds):
    '''Executes all rounds of the Pairs game and determines overall winners.

    Parameters:
        all_hands -- a list of dictionary objects representing all hands in play
        cards_per_hands -- int representing the total number of cards that should be dealt to each hand
        deck -- list of all available cards not currently in a hand
        number_of_rounds -- int representing the total number of rounds to play before the game ends
    Effects:
        The "wins" attribute of hands that were determined to win one or more rounds will be incremented accordingly
    '''
    for _ in range(number_of_rounds):
        play_hand(all_hands, cards_per_hand, deck)
        reset_all_hands(all_hands, deck)
    game_winners = find_overall_winners(all_hands)
    console_display.display_overall_winners(game_winners)

def reset_all_hands(hands, deck):
    '''Return all cards from all hands to the deck and reset round-based counters

    Parameters:
        hands -- a list of dictionary objects representing all hands in play
        deck -- list of all available cards not currently in a hand
    Effects:
        The "cards" attribute of each hand will be reset to an empty list
        All cards that were in a hand will be returned to the deck
    '''
    for hand in hands:
        deck.extend(hand['cards'])
        hand['cards'] = []
        hand['pairs'] = 0

def find_overall_winners(hands):
    most_wins = find_max_value_from_key('wins', hands)
    if most_wins == 0:
        return []
    return [hand for hand in hands if hand['wins'] == most_wins]