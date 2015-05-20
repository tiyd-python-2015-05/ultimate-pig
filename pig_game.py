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
        while self.go_again == True
            result = self.roll()
            if result == 1:
                self.go_again = False
                self.tally = 0
            else:
                self.add_tally(result)
                self.go_again = self.roll_again_logic()
        self.add_score()
        self.reset_after_turn()
        self.turn += 1


    def add_tally(self, roll):
        self.tally += roll

    def roll_again_logic(self):
        return False

    def reset_after_turn(self):
        self.roll_count = 0
        self.tally = 0
        self.go_again = True

    def game(self):
        while self.turn > 7:
            self.take_turn()
        return self.score




