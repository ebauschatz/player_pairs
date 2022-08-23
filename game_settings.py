def get_cards_per_hand():
    return 5

def get_number_of_each_type_in_deck():
    return 4

def get_card_types():
    return ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

def get_number_of_players():
    return get_valid_numeric_input('players')

def get_number_of_rounds():
    return get_valid_numeric_input('rounds')

def get_valid_numeric_input(input_type):
    valid_input = False
    while valid_input is False:
        user_value = input(f'Please enter the number of {input_type} for this game: ')
        if user_value.isnumeric() is True:
            return int(user_value)