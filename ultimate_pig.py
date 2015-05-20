import random
import sys

class Player(object):

    def __init__(self, total_score = 0, name="BasePlayer"):
        self.total_score = total_score
        self.name = name


    def __str__(self):
        return "{} with {} total score".format(self.name, self.total_score)


    def __repr__(self):
        return "Player: {}".format(self.name)


    @property
    def roll(self):
        random.seed()
        return random.randint(1,6)


    def hold(self):
        return True

    def update_score(self):
        score = self.roll
        if score != 1:
            self.total_score = self.total_score+score

    def print_score(self):
        return "Your total score was: {} point(s)".format(self.total_score)


    def play(self, rounds):
        current_turn = 0
        while current_turn < rounds:
            if self.roll != 1:
                self.update_score()
                current_turn += 1
            else:
                current_turn += 1
            print("This is turn {} with score {}".format(current_turn, self.total_score))


class Game(object):

    def __init__(self, current_player, rounds = 0, winning_score = 0 ):
        self.rounds = rounds
        self.winning_score = winning_score
        self.current_player = current_player


    def switch_player(self, player1, player2):
        if self.current_player == player1:
            self.current_player = player2
        else:
            self.current_player = player1


    def game(self):
        while this_round < self.rounds:
            player.play()



if __name__ == '__main__':
    player = Player()
    game = Game(current_player = player, rounds = 7)
    player.play(game.rounds)
    print(player.print_score())
