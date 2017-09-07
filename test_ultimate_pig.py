__author__ = 'willflowers'

from ultimate_pig import Game, Player, Player1, Player3, Player4

#test: These are the things I want to test

# if player is done (hold or keep going) (which player?)
#whether game has started
#what was rolled
#score adds
#game ends after 7 turns
#get data?

def test_is_player_done():
    player = Player1()
    player.rounds = 1
    assertTrue player.is_player_done

    player = Player3()
    player.rounds = 3
    assertTrue player.is_player_done

    player = Player4()
    player.rounds = 4
    assertTrue player.is_player_done

    player = Player4()
    player.rounds = 2
    assertFalse player.is_player_done


# def test_roll_counted():
