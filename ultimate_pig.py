import random


class Game:
    def __init__(self, player):
        self.player = player
        self.score = 0
        self.turns = 0

    def turn(self):
        self.score += self.player.play_turn()
        self.turns += 1

    def run(self, games=1):
        scores = []
        for n in range(games):
            self.reset()
            while self.turns < 7:
                self.turn()
            scores.append(self.score)
        return scores

    def reset(self):
        self.score = 0
        self.turns = 0


class Player:
    def __init__(self):
        self.rolls = 0

    def roll_die(self):
        roll = random.random()
        if roll < 0.167:
            return 1
        elif 0.167 <= roll < 0.333:
            return 2
        elif 0.333 <= roll < 0.5:
            return 3
        elif 0.5 <= roll < 0.667:
            return 4
        elif 0.667 <= roll < 0.833:
            return 5
        elif 0.833 <= roll <= 1.0:
            return 6

    def play_turn(self):
        turn_score = 0
        self.rolls = 0
        while self.decide(turn_score):
            roll = 0
            roll += self.roll_die()
            if roll == 1:
                turn_score = 0
                break
            else:
                turn_score += roll
            self.rolls += 1
        return turn_score

    def decide(self, score):
        if self.rolls < 1:
            return True
        else:
            return False


class Rolls5(Player):
    def decide(self, score):
        if self.rolls < 5:
            return True
        else:
            return False


class Until18(Player):
    def decide(self, score):
        if score < 18:
            return True
        else:
            return False


class PushIt(Player):
    def decide(self, score):
        if score < 30 and self.rolls < 10:
            return True
        else:
            return False


class Rolls4(Player):
    def decide(self, score):
        if self.rolls < 4:
            return True
        else:
            return False