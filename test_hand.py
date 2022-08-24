import hand

def test_track_wins_one_hand():
    hands = [
        {'name': 'test hand', 'cards': [], 'pairs': 0, 'wins': 0}
    ]
    hands_expected = [
        {'name': 'test hand', 'cards': [], 'pairs': 0, 'wins': 1}
    ]

    hand.track_wins(hands)
    assert hands == hands_expected

def test_track_wins_many_hands():
    hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 1},
        {'name': 'test hand 3', 'cards': [], 'pairs': 0, 'wins': 2}
    ]
    hands_expected = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 1},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 2},
        {'name': 'test hand 3', 'cards': [], 'pairs': 0, 'wins': 3}
    ]

    hand.track_wins(hands)
    assert hands == hands_expected

def test_track_wins_no_hands():
    hands = []
    hands_expected = []
    
    hand.track_wins(hands)
    assert hands == hands_expected

def test_find_max_value_from_key_single_option():
    test_dicts = [
        {'key1': 5, 'key2': 3}
    ]

    assert hand.find_max_value_from_key('key2', test_dicts) == 3

def test_find_max_value_from_key_multiple_options():
    test_dicts = [
        {'key1': 5, 'key2': 3},
        {'key1': 5, 'key2': 5},
        {'key1': 5, 'key2': 8},
        {'key1': 5, 'key2': 2}
    ]

    assert hand.find_max_value_from_key('key2', test_dicts) == 8

def test_find_max_value_from_key_all_options_same_value():
    test_dicts = [
        {'key1': 5, 'key2': 4},
        {'key1': 5, 'key2': 4},
        {'key1': 5, 'key2': 4},
        {'key1': 5, 'key2': 4}
    ]

    assert hand.find_max_value_from_key('key2', test_dicts) == 4

def test_determine_hand_winners_one_winner():
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 1, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 1, 'wins': 0},
        {'name': 'test hand 3', 'cards': [], 'pairs': 2, 'wins': 0}
    ]
    test_winning_hand = [{'name': 'test hand 3', 'cards': [], 'pairs': 2, 'wins': 0}]

    assert hand.determine_hand_winners(test_hands) == test_winning_hand

def test_determine_hand_winners_multiple_winners():
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 1, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 2, 'wins': 0},
        {'name': 'test hand 3', 'cards': [], 'pairs': 2, 'wins': 0}
    ]
    test_winning_hands = [
        {'name': 'test hand 2', 'cards': [], 'pairs': 2, 'wins': 0},
        {'name': 'test hand 3', 'cards': [], 'pairs': 2, 'wins': 0}
    ]

    assert hand.determine_hand_winners(test_hands) == test_winning_hands

def test_determine_hand_winners_no_winners():
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 3', 'cards': [], 'pairs': 0, 'wins': 0}
    ]

    assert hand.determine_hand_winners(test_hands) == []

def test_determine_pairs_in_hands_no_pairs():
    test_hands = [
        {'name': 'test hand 1', 'cards': ['ace', 'two', 'three', 'four', 'five'], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['ace', 'two', 'three', 'four', 'five'], 'pairs': 0, 'wins': 0}
    ]
    test_hands_expected = [
        {'name': 'test hand 1', 'cards': ['ace', 'two', 'three', 'four', 'five'], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['ace', 'two', 'three', 'four', 'five'], 'pairs': 0, 'wins': 0}
    ]

    hand.determine_pairs_in_hands(test_hands)
    assert test_hands == test_hands_expected

def test_determine_pairs_in_hands_at_least_one_pair():
    test_hands = [
        {'name': 'test hand 1', 'cards': ['ace', 'two', 'ace', 'four', 'five'], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['ace', 'two', 'three', 'three', 'two'], 'pairs': 0, 'wins': 0}
    ]
    test_hands_expected = [
        {'name': 'test hand 1', 'cards': ['ace', 'two', 'ace', 'four', 'five'], 'pairs': 1, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['ace', 'two', 'three', 'three', 'two'], 'pairs': 2, 'wins': 0}
    ]

    hand.determine_pairs_in_hands(test_hands)
    assert test_hands == test_hands_expected

def test_determine_pairs_in_hands_repeated_pair_cards():
    test_hands = [
        {'name': 'test hand 1', 'cards': ['ace', 'ace', 'ace', 'four', 'five'], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['two', 'two', 'two', 'three', 'three'], 'pairs': 0, 'wins': 0}
    ]
    test_hands_expected = [
        {'name': 'test hand 1', 'cards': ['ace', 'ace', 'ace', 'four', 'five'], 'pairs': 1, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['two', 'two', 'two', 'three', 'three'], 'pairs': 2, 'wins': 0}
    ]

    hand.determine_pairs_in_hands(test_hands)
    assert test_hands == test_hands_expected

def test_deal_cards_multiple_cards_per_hand():
    test_deck = ['ace', 'two', 'three', 'four', 'five', 'six']
    cards_per_hand = 3
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0}
    ]
    test_hands_expected = [
        {'name': 'test hand 1', 'cards': ['six', 'four', 'two'], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': ['five', 'three', 'ace'], 'pairs': 0, 'wins': 0}
    ]

    hand.deal_cards(test_hands, cards_per_hand, test_deck)
    assert test_hands == test_hands_expected

def test_deal_cards_remove_dealt_cards_from_deck():
    test_deck = ['ace', 'two', 'three', 'four', 'five', 'six']
    test_deck_expected = []
    cards_per_hand = 3
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0}
    ]

    hand.deal_cards(test_hands, cards_per_hand, test_deck)
    assert test_deck == test_deck_expected

def test_deal_cards_no_cards_per_hand():
    test_deck = ['ace', 'two', 'three', 'four', 'five', 'six']
    cards_per_hand = 0
    test_hands = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0}
    ]
    test_hands_expected = [
        {'name': 'test hand 1', 'cards': [], 'pairs': 0, 'wins': 0},
        {'name': 'test hand 2', 'cards': [], 'pairs': 0, 'wins': 0}
    ]

    hand.deal_cards(test_hands, cards_per_hand, test_deck)
    assert test_hands == test_hands_expected

def test_shuffle_deck_empty_deck():
    test_deck = []

    hand.shuffle_deck(test_deck)
    assert test_deck == []

def test_shuffle_deck_single_card_deck():
    test_deck = ['ace']
    test_deck_expected = ['ace']

    hand.shuffle_deck(test_deck)
    assert test_deck == test_deck_expected

def test_shuffle_deck_multiple_card_deck():
    test_deck = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    test_deck_original = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    test_deck_reshuffled = False
    shuffle_counter = 0
    while shuffle_counter < 1000 and test_deck_reshuffled is False:
        hand.shuffle_deck(test_deck)
        shuffle_counter += 1
        if test_deck != test_deck_original:
            test_deck_reshuffled = True
    assert test_deck_reshuffled