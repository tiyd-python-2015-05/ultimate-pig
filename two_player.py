import random
import math


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.record = [0, 0]

    def run(self, games=1):
        pointer = 0
        for n in range(games):
            self.score1 = 0
            self.score2 = 0
            while self.score1 < 100 and self.score2 < 100:
                if int(pointer) == 0:
                    self.score1 += self.player1.play_turn(self.score1, self.score2)
                    if self.score1 >= 100:
                        self.record[0] += 1
                        break
                else:
                    self.score2 += self.player2.play_turn(self.score2, self.score1)
                    if self.score2 >= 100:
                        self.record[1] += 1
                        break
                pointer = math.cos(pointer * (math.pi/2))
        return self.record



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

    def play_turn(self, your_score, their_score):
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
        if score < 20:
            return True
        else:
            return False


class Challenger(Player):
    def play_turn(self, your_score, their_score):
        self.rolls = 0
        if their_score > 75 and their_score - your_score > 10:
            turn_score = self.large_risk()
        elif their_score > 75 and their_score - your_score > 0:
            turn_score = self.small_risk()
        elif their_score > 50 and their_score - your_score > 10:
            turn_score = self.small_risk()
        elif their_score < 50 and their_score - your_score > 15:
            turn_score = self.small_risk()
        else:
            turn_score = self.play_it_safe()
        return turn_score

    def play_it_safe(self):
        score = 0
        while score < 20:
            roll = self.roll_die()
            if roll == 1:
                score = 0
                break
            else:
                score += roll
        return score

    def small_risk(self):
        score = 0
        while score < 25:
            roll = self.roll_die()
            if roll == 1:
                score = 0
                break
            else:
                score += roll
        return score

    def large_risk(self):
        score = 0
        while score < 35:
            roll = self.roll_die()
            if roll == 1:
                score = 0
                break
            else:
                score += roll
        return score


class Percentages(Player):
    def play_turn(self, your_score, their_score):
        self.rolls = 0
        if their_score/100 > your_score/(their_score + 0.1):
            turn_score = self.large_risk()
        else:
            turn_score = self.play_it_safe()
        return turn_score

    def play_it_safe(self):
        score = 0
        while score < 20:
            roll = self.roll_die()
            if roll == 1:
                score = 0
                break
            else:
                score += roll
        return score

    def large_risk(self):
        score = 0
        while score < 35:
            roll = self.roll_die()
            if roll == 1:
                score = 0
                break
            else:
                score += roll
        return score
