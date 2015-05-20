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
        num = self.roll()

        if num == 1:
            return self.score
        else:
            self.score += num

        return self.score

    def roll(self):
        return random.randint(1, 7)

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1

    def games(self):
        return self.losses + self.wins

    def new_game(self):
        self.score = 0


class SmartPlayer(Player):
    def __init__(self, name, brain, turn_lim=False):
        super().__init__(name)
        self.brain = brain
        self.turn_lim = turn_lim

    def turn(self):
        """
        uses the brain to roll
        with a strategy
        """
        if self.turn_lim:
            self.score += self.brain(self.turn_lim)
        else:
            self.score += self.brain()

        return self.score
