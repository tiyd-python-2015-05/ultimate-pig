from pig_player import PigPlayer, Die
from pig_game import PigSolitaire, PigGame


"""
Responsibilities:
    PigSolitaire is for 1 player, UltimatePig is for 2
    Tell player to start a new turn
    Track number of turns taken
    Collect score of player(s)
    Declare a winner if multiplayer
    X Declare game over if single player after n turns
        (Not needed, just stop asking for player turns)
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

def test_rigged_pig_game():
    good_die = Die(6,6)
    bad_die = Die(1,1)
    player1, player2 = PigPlayer(good_die), PigPlayer(bad_die)
    game = PigGame(player1, player2)
    winner = game.play()
    assert winner == (player1, 102)
    assert game.player2.score == 0

def test_normal_pig_game_series():
    die = Die()
    for _ in range(100):
        player1, player2 = PigPlayer(die), PigPlayer(die)
        game = PigGame(player1, player2)
        winner = game.play()
        assert winner[1] >= 100
        assert game.loser[1] < 100
        print('Winner: {},  Loser: {}'.format(winner[0], game.loser[0]))
