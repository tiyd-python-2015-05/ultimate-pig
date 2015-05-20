import random

class Player:
    """Player has 7 turns and tries to get the highest score."""
    def __init__(self):
        self.score = 0
        self.turn = 0
        self.tally = 0
        self.roll_count = 0
        self.go_again = True


    def roll(self):
        self.roll_count += 1
        return random.randint(1,6)


    def add_score(self):
        self.score += self.tally


    def take_turn(self):
        self.turn += 1


    def add_tally(self, roll):
        self.tally += roll

    def roll_again_logic(self):
        return False

