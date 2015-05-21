"""
 Responsibilities:
    Decide behavior based on number of players
    Tell player to start a new turn
    Track number of turns taken
    Collect score of player(s)
    Declare a winner if mulitplayer
    Declare game over if single player after n turns
"""
class PigSolitaire():
    """Takes a single player"""
    def __init__(self, player, total_rounds=7):
        self.player = player
        self.done = False
        self.rounds_complete = 0
        self.total_rounds = total_rounds

    def play(self):
        score = 0
        while self.rounds_complete < self.total_rounds:
            score = self.player.take_turn()
            self.rounds_complete += 1
        return score

if __name__ == '__main__':
    import pig_player as pp
    die = pp.Die()
    player = pp.PigPlayer(die, verbose=True)
    game = PigSolitaire(player)
    print(game.play())
