# # ## Work or sleep in

# from operator import truediv


# day = input('(*stumbling to turn off alarm clock*) what day is it? ')
# day_lower = day.lower().capitalize()

# if day_lower == 'Monday' or day_lower == 'Tuesday' or day_lower == 'Wednesday' or day_lower == 'Thursday' or day_lower == 'Friday':
#     print('Time to go to work!')
# elif day_lower == 'Saturday' or day_lower == 'Sunday':
#     print("Sleep in! It's the weekend!")
# else:
#     print('Please enter a valid day.')


# ## Secret password

# password = input('Password: ')

# if password == 'thewitchinghour':
#     print('Welcome back!')
# else:
#     print('Password incorrect, please try again.')


# ## Day of the Week

# dow = int(input('What number?: '))
# if dow == 1:
#     print('Sunday')
# elif dow == 2:
#     print('Monday')
# elif dow == 3:
#     print('Tuesday')
# elif dow == 4:
#     print('Wednesday')
# elif dow == 5:
#     print('Thursday')
# elif dow == 6:
#     print('Friday')
# elif dow == 7:
#     print('Saturday')
# else:
#     print('Error, please pick a valid number.')

# # Letter Grade

# grade = int(input('What score did you get?: '))

# if grade <= 59 and grade >= 0:
#     print('F')
# elif grade >= 60 and grade <= 69:
#     print('D')
# elif grade >= 70 and grade <= 79:
#     print('C')
# elif grade >= 80 and grade <= 89:
#     print('B')
# elif grade >= 90 and grade <= 100:
#     print('A')
# else:
#     print('Invalid number')

# ## Picnic Game

# def picnic_game(str1, str2):
#     if str1[0] == str2[0]:
#         return True
#     else:
#         return False
# name = input('What is your name?: ')
# food_q = input('What food are your bringing?: ')


# if picnic_game(name, food_q) == True:
#     print('You can come to the picnic!')
# else: 
#     print('Please try again')




def number_div(num):
    if num % 2 != 0 and num % 3 == 0:
        print(True)
    else:
        print(False)
enter_num = int(input('Enter a number: '))

number_div(enter_num)
