def get_cards_per_hand():
    return 5

def get_number_of_each_type_in_deck():
    return 4

def get_number_of_players():
    valid_input = False
    while valid_input is False:
        players = input('Please enter the number of players for this game: ')
        if players.isnumeric() is True:
            return int(players)

def get_card_types():
    return ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']