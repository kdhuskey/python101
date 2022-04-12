# exponent = ['*', '*', '*', '*', '*']


# for i in exponent:
#     print(exponent)
# ## Print a square
# exponent = '*****'
# for i in range(5):
#     print(exponent)


# ## Print a Triangle
# height = int(input('How tall are you?'))
# for i in range(0, height):
#     spaces = height - 1 - i
#     stars = i * 2 + 1
#     print(" " * spaces + "*" * stars)

# ## Multiplication Tables

# for num_1 in range(1, 11):
#     for num_2 in range(1, 11):
#         answer = num_1 * num_2
#         print (f"{num_1} * {num_2} = {answer}")


# # Print a Box

# width_1 = int(input('How wide is it?: '))
# height_1 = int(input('How tall is it?: '))
# variable = '*'
# for i in range(width_1, height_1):
#     print(variable)



#     spaces = height_1 - 1 - i
#     stars = i * 2 + 1
#     print(" " * width_1 * height_1)



## Coin Flipper
import random
num = 1
num_coins = print(f'You have {num} coin.')
question = input('Do you want another? ')

def coin_flip():
    flip = random.randint(0,1)
    if flip == 0:
        print(f'Coin {num} - Heads')
    else:
        print(f'Coin {num} - Tails')

while question == 'yes':
    for total_coins in range(num):
        if question == 'yes':
            num += 1
            print(f'You have {num} coins.')
        elif question == 'no':
            print(f'Ok you have {num} coins!, now let us flip them.')
            
        coin_flip()

