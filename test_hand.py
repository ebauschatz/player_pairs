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