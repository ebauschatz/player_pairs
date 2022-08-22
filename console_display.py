def display_welcome_message(number_of_cards):
    print(f'''Welcome to Player Pairs!
    In this game each player will receive {number_of_cards} cards.
    Once each hand has been dealt, we will compare to see who has the most pairs!''')

def display_all_hands(hands):
    for hand in hands:
        print(f'\n{hand["name"]}')
        print(f'Hand: {hand["cards"]}')
        print(f'Number of Pairs: {hand["pairs"]}')