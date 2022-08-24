import game

def test_find_overall_winners_no_winners():
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0}
    ]

    assert game.find_overall_winners(test_hands) == []

def test_find_overall_winners_one_winner():
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 1}
    ]
    winners_expected = [{'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 1}]

    assert game.find_overall_winners(test_hands) == winners_expected

def test_find_overall_winners_multiple_winners():
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 1},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 1}
    ]
    winners_expected = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 1},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 1}
    ]

    assert game.find_overall_winners(test_hands) == winners_expected

def test_reset_all_hands_cards_removed():
    test_deck = ['ace', 'two', 'three', 'four', 'five', 'six']
    test_hands = [
        {'name': 'test hand 1', 'cards': ['jack', 'queen', 'king'], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['seven', 'eight', 'nine'], 'pairs': 0, 'wins': 0}
    ]
    test_hands_expected = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0}
    ]

    game.reset_all_hands(test_hands, test_deck)
    assert test_hands == test_hands_expected

def test_reset_all_hands_pairs_reset():
    test_deck = ['ace', 'two', 'three', 'four', 'five', 'six']
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 1, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 2, 'wins': 0}
    ]
    test_hands_expected = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0}
    ]

    game.reset_all_hands(test_hands, test_deck)
    assert test_hands == test_hands_expected

def test_reset_all_hands_cards_added_back_to_deck():
    test_deck = ['ace', 'two', 'three', 'four', 'five', 'six']
    test_deck_expected = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen']
    test_hands = [
        {'name': 'test hand 1', 'cards': ['seven', 'eight', 'nine'], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['ten', 'jack', 'queen'], 'pairs': 0, 'wins': 0}
    ]

    game.reset_all_hands(test_hands, test_deck)
    assert test_deck == test_deck_expected