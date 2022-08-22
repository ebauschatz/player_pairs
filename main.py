import random
import console_display

def main():
    cards_per_hand = 5
    number_of_each_type_in_deck = 4
    console_display.display_welcome_message(cards_per_hand)
    deck = generate_deck(number_of_each_type_in_deck)
    shuffle_deck(deck)
    #deal hands to players
    #determine pairs per hand
    #display hands and pairs per hand
    #determine and display the winner(s)

def generate_deck(type_repetitions):
    card_types = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    new_deck = []
    new_deck.extend(card_types * type_repetitions)
    return new_deck

def shuffle_deck(deck):
    random.shuffle(deck)

main()