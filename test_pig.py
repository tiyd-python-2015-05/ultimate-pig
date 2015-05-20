import nose
from nose.tools import raises

from pig import Pig, Player

def test_new_pig():
    pig = Pig(turn_lim=6)
    assert pig.turn_lim == 6

@raises(KeyError)
def test_bad_pig():
    pig = Pig()

@raises(KeyError)
def test_2bad_big():
    pig = Pig(6,5)

def test_new_player():
    player = Player("Johan")
    assert player.name == "Johan"

def test_set_switch_players():
    player = Player("Johan")
    player2 = Player("Gilgamesh")
    pig = Pig(turn_lim=6)
    pig.set_players(player, player2)
    assert len(pig.players) == 2
    assert pig.players[0].name == "Johan"
    assert pig.players[1].name == "Gilgamesh"
    assert pig.current_player.name == "Johan"

    pig.switch_players()
    assert pig.current_player.name == "Gilgamesh"

def test_turn():
    player = Player("Johan")
    player2 = Player("Gilgamesh")
    pig = Pig(turn_lim=6)
    pig.set_players(player, player2)

    for _ in range(100):
        pig.turn()

    assert pig.scores["Johan"] > 0 or pig.scores["Gilgamesh"] > 0


def test_new_game():
    player = Player("Johan")
    player2 = Player("Gilgamesh")
    pig = Pig(turn_lim=6)
    pig.set_players(player, player2)

    for _ in range(6):
        pig.turn()

    pig.new_game()

    for item in pig.scores:
        assert pig.scores[item] == 0

def test_win_new_game():
    pig = Pig(score_lim=1)
    player = Player("Johan")
    player2 = Player("Gilgamesh")
    pig.set_players(player, player2)
    pig.scores["Johan"] = 1

    assert pig.check_win() == "Johan"
    assert player.wins == 1

    pig.new_game()

    assert player.score == 0

if __name__ == '__main__':
    nose.main()
