from flip_coin import coin_flip
from roll_die import dice_roll, multi_dice



print("""
Please choose an option:
1 - Flip a coin
2 - Roll a die
3 - Multiple die
Q - Exit""")

user_choice = input('')

def main():
    if user_choice == '1':
        coin_flip()
    elif user_choice == '2':
        dice_roll()
    elif user_choice == '3':
        multi_dice()
    elif user_choice == 'Q' or user_choice == 'q':
        print('EXIT')
    else:
        exit
main()
# coin_flip()


import arrow
