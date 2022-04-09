# ## Count to X
# user_number = int(input('Enter a Number: '))
# count = 1
# while count <= user_number:
#     print(count)
#     count += 1

## Count N to M

# num_1 = int(input('Enter a Number: '))
# num_2 = int(input('Enter another Number: '))

# if num_1 < num_2:
#     while num_1 <= num_2:
#         print(num_1)
#         num_1 += 1

# elif num_1 > num_2:
#     while num_1 >= num_2:
#         print(num_1)
#         num_1 -= 1

# Count odd N to M



# num_1 = int(input('Enter a Number1: '))
# num_2 = int(input('Enter another Number2: '))

# if num_1 < num_2:
#     while num_1 <= num_2:
#         if num_1 % 2 != 0:
#             print(num_1)
#         num_1 += 1


# elif num_2 < num_1:
#     while num_2 <= num_1:
#         if num_2 % 2 != 0:
#             print(num_2)
#         num_2 += 1

## FizzBuzz

user_input = int(input('Enter a Number: '))
count = 0

while count < user_input:
    if (count + 1) % 3 == 0 and (count + 1) % 5 == 0:
        print('fizzbuzz')
        count += 1
    elif (count + 1) % 3 == 0:
        print('fizz')
        count += 1
    elif (count + 1) % 5 == 0:
        print('buzz')
        count += 1
    
    print(count)
    count += 1
