import random
import statistics as st


class Player:
    """Player has 7 turns and tries to get the highest score."""
    def __init__(self):
        self.score = 0
        self.turn = 0
        self.tally = 0
        self.roll_count = 0
        self.go_again = True


    def roll(self):
        """Player rolls die and returns a value, also increments roll count for turn."""
        self.roll_count += 1
        return random.randint(1,6)


    def add_score(self):
        """At end of each turn, player adds tally from turn to total score."""
        self.score += self.tally


    def take_turn(self):
        """Player takes turn.  Continues to play as long as self.go_again is True.
        Roll again logic determines if player rolls again after successful roll"""
        while self.go_again == True:
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
        """Adds roll total to tally after roll."""
        self.tally += roll


    def roll_again_logic(self):
        """The roll again logic for the base player is to only roll once."""
        return False


    def reset_after_turn(self):
        """Reset turn specific info after turn complete."""
        self.roll_count = 0
        self.tally = 0
        self.go_again = True


    def game(self):
        """Game runs while player is on turn 0 through 6"""
        self.score = 0
        self.turn = 0
        while self.turn < 7:
            self.take_turn()
        return self.score


class Three_Rolls_Player(Player):
    """This player will roll three times every time  -- or bust."""
    def roll_again_logic(self):
        if self.roll_count == 3:
            return False
        else:
            return True


class Two_Rolls_Player(Player):
    def roll_again_logic(self):
        if self.roll_count == 2:
            return False
        else:
            return True


class Four_Rolls_Player(Player):
    def roll_again_logic(self):
        if self.roll_count == 4:
            return False
        else:
            return True

class Five_Rolls_Player(Player):
    def roll_again_logic(self):
        if self.roll_count == 5:
            return False
        else:
            return True

class Six_Rolls_Player(Player):
    def roll_again_logic(self):
        if self.roll_count == 6:
            return False
        else:
            return True


class Roll_Until_10_Player(Player):
    def roll_again_logic(self):
        if self.tally < 10:
            return True
        else:
            return False


class Roll_Until_15_Player(Player):
    def roll_again_logic(self):
        if self.tally < 15:
            return True
        else:
            return False


class Roll_Until_20_Player(Player):
    def roll_again_logic(self):
        if self.tally < 20:
            return True
        else:
            return False


class Roll_Until_30_Player(Player):
    def roll_again_logic(self):
        if self.tally < 30:
            return True
        else:
            return False

class Roll_Until_40_Player(Player):
    def roll_again_logic(self):
        if self.tally < 40:
            return True
        else:
            return False

def n_trials(n, player_type=Player):
    results = []
    player1 = player_type()
    for _ in range(n):
        results.append(player1.game())
    return (st.mean(results), st.stdev(results), max(results),
            min(results), results)





