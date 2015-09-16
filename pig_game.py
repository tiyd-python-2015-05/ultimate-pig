import random

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

class PigGame():
    """Takes two players"""
    def __init__(self, player1, player2, winning_score=100):
        self.player1 = player1
        self.player2 = player2
        self.current_player = random.choice([player1, player2])
        self.done = False
        self.rounds_complete = 0
        self.winner = None
        self.loser = None

    def play(self):
        score = 0
        while self.winner is None:
            score = self.current_player.take_turn()
            self.rounds_complete += 0.5
            if score >= 100:
                self.winner = (self.current_player, score)
                loser = self.next_player()
                self.loser = (loser, loser.score)
                return self.winner
            else:
                self.current_player = self.next_player()

    def next_player(self):
        if self.current_player is self.player1:
            return self.player2
        return self.player1

if __name__ == '__main__':
    import pig_player as pp
    die = pp.Die()
    player = pp.PigPlayer(die, verbose=True)
    game = PigSolitaire(player)
    print(game.play())
