__author__ = 'willflowers'


import random


class Game:

    def __init__(self, player):
        self.player = player

    def start(self):
        player = Player()

        if self.player.turns <= 8:
            player.start()
        else:
            return self.player.score



class Player:

    def __init__(self):
        self.score = 0
        self.rolls = 0
        self.turns = 0
        self.rounds = 0
        self.turn_score = 0
        self.turn_over = False


    def turn(self):
        if self.turn_over == True:
            self.score += self.turn_score
            self.turns += 1


    def round(self):
        self.roll = random.randint(1, 6)
        if self.roll == 1:
            self.turn_score = 0
            self.turn_over = True
            self.turn()
        else:
            self.turn_score += self.roll
            self.rounds += 1

    def start(self):
        while not self.turn_over:
            self.round()


    def turn(self):
        if self.turn_over == True:
            self.score += self.turn_score
            self.turnscore = 0
            self.turns += 1









#Will roll once every turn
class Player1(Player):
    def is_player_done(self):
        if self.rounds == 1:
            self.turn_over = True
            self.turn()

#Will roll three times if possible every turn
class Player3(Player):

    def is_player_done(self):
        if self.rounds == 3:
            self.turn_over = True
            self.turn()

#Will roll four times if possible every turn
class Player4(Player):

    def is_player_done(self):
        if self.rounds == 4:
            self.turn_over = True
            self.turn()


if __name__ == '__main__':
    will = Player3()
    game = Game(will)
    print(game.start())