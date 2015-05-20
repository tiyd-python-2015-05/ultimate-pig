import random

class Die():
    def __init__(self, minimum=1, maximum=6):
        self.minimum = minimum
        self.maximum = maximum
    def roll(self):
        """Returns value of a die roll with minimum and maximum # of dots"""
        return random.randint(self.minimum, self.maximum)


class PigPlayer():
    """
    Responsibilities:
          Track total score
          When prompted to start the turn, roll the die
          End turn on a 1, without adding to score
          Track turn score
          Decide to roll again or hold
          Signal end of a turn to Game
    """
    def __init__(self, die):
        self.score = 0
        self.turn_score = 0
        self.die = die
        self.turn_over = False
        self.num_rolls = 0

    def roll_die(self):
        return self.die.roll()

    def do_roll(self):
        """Roll die and add roll points/set turn_over depending on result"""
        roll_points = self.roll_die()
        if roll_points == 1:
            self.turn_over = True
            roll_points == 0
        else:
            self.turn_over = False
        self.turn_score += roll_points
        self.num_rolls += 1

    def hold(self):
        """Stop rolling, collect points, end the turn"""
        self.score += self.turn_score
        self.turn_score = 0
        self.turn_over = True

    def decide(self, num_turns=1):
        """
        Use a strategy to determine whether to roll or hold
        Basic strategy is to hold after num_turns turns
        More advanced strategies are incorporated into subclasses
        """
        if self.num_rolls == num_turns:
            self.hold()
        else:
            self.do_roll()

    def take_turn(self):
        """
        The main loop for a single turn from start to finish
        Return False when the player is done
        """
        # remember to set turn_over to True initially
        while not self.turn_over:
            self.decide()
