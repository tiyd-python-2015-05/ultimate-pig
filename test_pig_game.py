from pig_player import PigPlayer, Die
from pig_game import PigSolitaire


"""
Responsibilities:
    PigSolitaire is for 1 player, UltimatePig is for 2
    Tell player to start a new turn
    Track number of turns taken
    Collect score of player(s)
    Declare a winner if mulitplayer
    Declare game over if single player after n turns
"""

def test_pig_solitaire_creation():
    die = Die()
    player = PigPlayer(die)
    game = PigSolitaire(player)
    assert game.player == player
    assert game.done == False
    assert game.rounds_complete == 0

def test_solitaire_play():
    die = Die(3,3)
    player = PigPlayer(die)
    game = PigSolitaire(player)
    score = game.play()
    assert score == 3*7
