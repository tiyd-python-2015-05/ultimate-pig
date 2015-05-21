import random


def simple_threshold(k=.5, score_lim=False, turn_lim=False):

    def func(score, turn=False):

        nonlocal k

        roll = random.randint(1, 6)
        num_rolls = 1
        final = roll

        while roll != 1:

            if k > (5/6)**num_rolls:
                return final

            num_rolls +=1
            roll = random.randint(1, 6)
            final += roll

        return 0

    return func


def complex_threshold(k=.5, score_lim=False, turn_lim=False):

    def func(score, turn=False):

        nonlocal k
        nonlocal score_lim

        thresh = k + k/(score_lim - score + 1)

        roll = random.randint(1, 6)
        num_rolls = 1
        final = roll

        while roll !=1:

            if thresh > (5/6)**num_rolls:
                return final

            roll = random.randint(1, 6)
            final += roll
            num_rolls += 1

        return 0

    return func
