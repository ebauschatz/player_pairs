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