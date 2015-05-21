from ultimate_pig import Game, Player
from unittest import mock


def test_game_has_score():
    player = Player()
    game = Game(player)
    assert game.score == 0

def test_game_has_turns():
    player = Player()
    game = Game(player)
    assert game.turns == 0
    game.turn()
    assert game.turns == 1

def test_game_runs_for_7_turns():
    player = Player()
    game = Game(player)
    game.run()

    assert game.turns == 7

def test_game_add_player_score():
    with mock.patch("random.random", return_value=1):
        player = Player()
        game = Game(player)
        starting_score = game.score
        game.turn()

    assert game.score != starting_score

def test_game_can_reset():
    player = Player()
    game = Game(player)
    game.turn()
    game.reset()
    assert game.turns == 0

def test_game_can_run_multiple_times():
    player = Player()
    game = Game(player)
    assert len(game.run(games=3)) == 3
