def display_welcome_message(number_of_cards):
    print(f'''\nWelcome to Player Pairs!
    In this game each player will receive {number_of_cards} cards.
    Once each hand has been dealt, we will compare to see who has the most pairs!''')

def display_all_hands(hands):
    for hand in hands:
        print(f'\n{hand["name"]}')
        print(f'Hand: {hand["cards"]}')
        print(f'Number of Pairs: {hand["pairs"]}')

def display_hand_winners(winning_hands):
    print('\nRound result: ')
    display_winners(winning_hands, 'pair', 'pairs')

def display_overall_winners(winning_hands):
    print('\nOverall game result:')
    display_winners(winning_hands, 'win', 'wins')

def display_winners(winning_hands, win_condition_display, key):
    number_of_winners = len(winning_hands)
    if number_of_winners == 0:
        print(f'No players had any {win_condition_display}s')
    elif number_of_winners == 1:
        print(f'{winning_hands[0]["name"]} has won with {winning_hands[0][key]} {win_condition_display}(s)!')
    else:
        print(f'There was a {number_of_winners}-way tie between the below players with {winning_hands[0][key]} {win_condition_display}(s)!')
        for hand in winning_hands:
            print(hand['name'])