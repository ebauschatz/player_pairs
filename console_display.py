def display_welcome_message(number_of_cards):
    print(f'''Welcome to Player Pairs!
    In this game each player will receive {number_of_cards} cards.
    Once each hand has been dealt, we will compare to see who has the most pairs!''')

def display_all_hands(hands):
    for hand in hands:
        print(f'\n{hand["name"]}')
        print(f'Hand: {hand["cards"]}')
        print(f'Number of Pairs: {hand["pairs"]}')

def display_all_winners(winning_hands):
    number_of_winners = len(winning_hands)
    if number_of_winners == 0:
        print('No players had any pairs in their hand.')
    elif number_of_winners == 1:
        print(f'\n{winning_hands[0]["name"]} has won with {winning_hands[0]["pairs"]} pair(s)!')
    else:
        print(f'\nThere was a {number_of_winners}-way tie between the below players with {winning_hands[0]["pairs"]} pair(s)!')
        for hand in winning_hands:
            print(hand['name'])