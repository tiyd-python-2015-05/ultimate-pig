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
        self.current_player = 0
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
        self.current_player = 0

    def check_win(self):
        """
        checks the win conditions,
        notifies winner and
        returns winner name if game is done
        """
        if self.score_lim == False:
            if self.turn_lim == self.current_turn:
                name = max(self.scores.items(), key=itemgetter(1))
                return name[0]

            return False
        else:
            name = max(self.scores.items(), key=itemgetter(1))
            if self.score_lim <= self.scores[name[0]]:
                return name[0]

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
        self.current_player = None

    def create_players(self, what, thresh):
        """
        Adds a preset player type
        to the game.  Choices
        are simple, complex, and random
        """

        if len(what) -  what.count("Random") != len(thresh):
            raise KeyError("number of items requiring a threshold does \
                            not match number of thresholds")

        new_player = []

        while "Random" in what:
            what.pop("Random")
            new_player.append(Player("Random {}".format(random.randint(0,115))))

        for idx in range(len(what)):
            if what[idx] == "complex":
                new_player.append(SmartPlayer(
                            "Jean-Luc Picard {}".format(random.randint(0,115)),
                            complex_threshold(thresh[idx]), self.score_lim))

            if what[idx] == "simple":
                new_player.append(SmartPlayer(
                                "Gilgamesh {}".format(random.randint(0,115)),
                                                simple_threshold(thresh[idx])))

        self.set_players(*new_player)
