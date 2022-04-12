import random

def coin_flip():
    flip = random.randint(0,1)
    if flip == 0:
        print("""You flipped a coin!
        It is heads!""")
    else:
        print("""You flipped a coin!
        It is tails!""")

coin_flip()



## Even odd

def even_odd(choice):
    if choice % 2 != 0:
        print("It's Odd!")
    else:
        print("It's Even!")

choice = int(input('Enter a number: '))
even_odd(choice)


# Dice Roller


die_question = int(input("""Let's roll a dice!
How many sides should it have? (2-20): """))

def dice_roll(die_question):
    roll = random.randint(1, die_question)
    print(f'It is a {roll} !')
    #return roll 

dice_roll(die_question)



