import random

def coinflip():
    random.seed()
    if random.random() < 0.5:
        ret = "Heads"
    else:
        ret = "Tails"
    return ret
