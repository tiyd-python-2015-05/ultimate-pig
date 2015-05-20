import random
from operator import itemgetter
from players import Player, SmartPlayer
from strategies import simple_threshold, complex_threshold


class Pig:
    """
    a game of pig
    with two players
    and either a turn limit
    or a score limit
    """
    def __init__(self, turn_lim=False, score_lim=False):
        """
        defaults to 7 turn limit game
        """
        if not turn_lim and not score_lim or (turn_lim and score_lim):
            raise KeyError("Pig must have turn or score limit")

        self.turn_lim = turn_lim
        self.score_lim = score_lim

        self.players = []
        self.current_player = None
        self.scores = {}
        self.current_turn = 0

    def set_players(self, *players):
        """
        sets the list of players
        and initializes them with
        a score of 0
        """
        self.players = players
        self.current_player = self.players[0]
        self.scores = {player.name: 0 for player in self.players}

    def turn(self):
        """
        the current player
        takes a turn and the result
        is recorded in scores,
        then a new current player
        is set
        """
        player = self.players[self.current_player]
        new_val = player.turn()
        self.scores[player.name] = new_val
        self.switch_players()
        self.current_turn += 1

    def switch_players(self):
        """
        updates the current player
        cycling through a list of players
        """
        if self.current_player == len(self.players) - 1:
            self.current_player = 0

        else:
            self.current_player += 1

    def new_game(self):
        """
        resets the scores
        of the players
        """
        self.scores = {item: 0 for item in self.scores}
        for player in self.players:
            player.new_game()
        self.current_turn = 0

    def check_win(self):
        """
        checks the win conditions,
        notifies winner and
        returns winner name if game is done
        """
        if self.score_lim == False:
            if self.turn_lim == self.current_turn:
                name = max(self.scores, key=itemgetter(1))
                return name

            return False
        else:
            name = max(self.scores, key=itemgetter(1))
            if self.score_lim <= self.scores[name]:
                return name

            return False

    def tell(self, name):
        """
        notifies the player
        whose name is given
        that they won the game
        """
        for player in self.players:
            if player.name == name:
                player.win()
            else:
                player.lose()

    def loop(self):
        while not self.check_win():
            self.turn()

        self.tell(self.check_win())

    def clear_players(self):
        self.players = []
        self.scores = {}

    def create_player(self, *what):
        """
        Adds a preset player type
        to the game.  Choices
        are simple, complex, and random
        """

        if what[0] == "complex":
            if len(what) == 2:
                thresh = what[1]
                self.players.append(SmartPlayer("Jean-Luc Picard",
                                    complex_threshold(thresh), self.score_lim))
            else:
                self.players.append(SmartPlayer("Jean-Luc Picard",
                                    complex_threshold(), self.score_lim))

        if what[0] == "simple":
            if len(what) == 2:
                thresh = what[1]
                self.players.append(SmartPlayer("Gilgamesh",
                                                simple_threshold(thresh)))
            else:
                self.players.append(SmartPlayer("Gilgamesh",
                                                simple_threshold()))

        if what[0] == "random":
            self.players.append(Player("Random"))

        self.current_player = self.players[0]

        for player in self.players:
            self.scores[player.name] = 0
