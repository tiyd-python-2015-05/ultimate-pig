import pig_player
"""
Responsibilities:
  Player:
      Track total score
      When prompted to start the turn, roll the die
      End turn on a 1, without adding to score
      Track turn score
      Decide to roll again or hold
"""
def test_player_starts_with_0_score():
    player = PigPlayer()
    assert player.score == 0
    assert player.turn_score == 0
