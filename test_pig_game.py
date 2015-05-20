__author__ = 'joshuahiggins'
from pig_game import Player
import pytest

def test_player_init():
    player1 = Player()
    assert player1.score == 0

def test_roll():
    player1 = Player()
    roll_test = player1.roll()
    assert 1 <= roll_test <= 6

def test_turn_increments_turn():
    player1 = Player()
    player1.take_turn()
    assert player1.turn == 1

def test_add_score():
    player1 = Player()
    player1.tally = 25
    player1.add_score()
    assert player1.score == 25

def test_add_tally():
    player1 = Player()
    player1.add_tally(5)
    assert player1.tally == 5

def test_roll_increases_roll_count():
    player1 = Player()
    player1.roll()
    assert player1.roll_count == 1

def test_player_roll_again_logic():
    player1 = Player()
    assert not player1.roll_again_logic()