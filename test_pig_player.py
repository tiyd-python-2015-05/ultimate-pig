from pig_player import PigPlayer, Die
"""
Responsibilities:
      Track total score
      When prompted to start the turn, roll the die
      End turn on a 1, without adding to score
      Track turn score
      Decide to roll again or hold
"""
def make_player():
    die = Die()
    return PigPlayer(die)

def make_player_3_die():
    die_3 = Die(3,3)
    return PigPlayer(die_3)

def test_player_starts_with_0_score():
    player = make_player()
    assert player.score == 0
    assert player.turn_score == 0


def test_player_default_roll_has_1_through_6():
    player = make_player()
    rolls = []
    for _ in range(100):
        # All rolls are between 1 and 6 inclusive
        rolls.append(player.roll_die())
        assert rolls[-1] in range(1,7)
    for n in range(1,7):
        # Each value appears at least once over 100 rolls
        assert n in rolls

def test_player_accumulates_points_if_not_1():
    player = make_player_3_die()
    assert player.turn_score == 0
    player.do_roll()
    assert player.turn_score == 3
    player.do_roll()
    assert player.turn_score == 6

def test_player_accumulates_turns():
    player = make_player()
    player.do_roll()
    assert player.num_rolls == 1
    for _ in range(99):
        player.do_roll()
    assert player.num_rolls == 100

def test_player_score_increases_turn_over_on_hold():
    player = make_player_3_die()
    player.do_roll()
    assert player.turn_over == False
    assert player.turn_score == 3
    assert player.score == 0
    player.hold()
    assert player.turn_score == 0
    assert player.score == 3
    assert player.turn_over == True

    # self.score = 0
    # self.turn_over = False
