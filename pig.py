import random
from operator import itemgetter


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
        if not turn_lim:
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
        new_val = self.current_player.turn()
        self.scores[self.current_player.name] = new_val
        self.switch_players()
        self.current_turn += 1

    def switch_players(self):
        """
        updates the current player
        cycling through a list of players
        """
        if self.players.index(self.current_player) == len(self.players) - 1:
            self.current_player = self.players[0]

        self.current_player = \
            self.players[self.players.index(self.current_player) + 1]

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
                max(scores, key=itemgetter[1])
                self.tell(name)
                return name

            return False
        else:
            name = max(self.scores, key=itemgetter(1))
            if self.score_lim <= self.scores[name]:
                self.tell(name)
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


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.score = 0

    def turn(self):
        self.score += random.randint(0, 100)
        return self.score

    def win(self):
        self.wins += 1

    def new_game(self):
        self.score = 0
