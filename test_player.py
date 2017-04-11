from ultimate_pig import Player, Rolls5, Until18, PushIt
from unittest import mock

def test_player_rolls_die():
    player = Player()
    assert 6 >= player.roll_die() > 0

def test_player_returns_score():
    player = Player()
    assert type(player.play_turn()) == int

def test_player_rolls_once_per_turn():
    player = Player()
    assert player.play_turn() < 7

def test_player_scores_zero_on_roll_of_one():
    with mock.patch("random.random", return_value=0):
        player = Player()
        assert player.play_turn() == 0

def test_subclasses():
    with mock.patch("random.random", return_value=1):
        player = Rolls5()
        assert player.play_turn() == 30