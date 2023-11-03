# this file contains the get_ord function where based on the game level function return the word
import random


def get_word(level):
    # check the level is easy
    if level == 1:
        easy_list = ['hello', 'dream', 'happy']
        # return a random word from the easy_list
        return random.choice(easy_list)
    # check the level is medium
    elif level == 2:
        medium_list = ['rainbow', 'beautiful', 'helpful']
        # return a random word from the medium_list
        return random.choice(medium_list)
    # check the level is difficult
    elif level == 3:
        difficult_list = ['temporary', 'monopoly', 'justification']
        # return a random word from the difficult_list
        return random.choice(difficult_list)
    else:
        # if not a valid choice return none
        return None
