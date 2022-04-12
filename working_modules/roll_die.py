import random

def dice_roll():
    die_question = int(input("""Let's roll a dice! \nWhich number are you betting it will land on? (1-6): """))
    roll = random.randint(1, 6)
    if die_question < 1 or die_question > 7:
        print('Sorry that number can not be reached with one die.')
    else:
        print(f'It is a {roll} !')

def multi_dice():
    many_d = int(input('How many dice are you wanting to throw? '))
    many_side = int(input('How many sides are they? '))
    total = many_d * many_side
    input('Ok! Lets roll some dice, What number are you betting they will land on? ')
    
    roll = random.randint(1, total)
    print(f'They are...  {roll}!!')




