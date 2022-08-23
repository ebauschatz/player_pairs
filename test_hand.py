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