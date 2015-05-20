import random

class Player:
    """
    basic player with stats
    never holds
    """
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.score = 0
        self.losses = 0

    def turn(self):
        num = random.randint(1, 6)

        if num == 1:
            return self.score
        else:
            self.score += num

        return self.score

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1

    def games(self):
        return self.losses + self.wins

    def new_game(self):
        self.score = 0


class SmartPlayer(Player):
    def __init__(self, name, brain, score_lim=False, turn_lim=False):
        super().__init__(name)
        self.brain = brain
        self.turn_lim = turn_lim
        self.score_lim = score_lim
        self.current_turn = 0

    def turn(self):
        """
        uses the brain to roll
        with a strategy
        """
        self.current_turn += 1

        if self.turn_lim:
            self.score += self.brain(self.score)
        else:
            self.score += self.brain(self.score)

        return self.score
