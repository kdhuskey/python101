import random
def coin_flip():
    flip = random.randint(0,1)
    if flip == 0:
        print('You flipped a coin! \nIt is heads!')
    else:
        print("""You flipped a coin! \nIt is tails!""")