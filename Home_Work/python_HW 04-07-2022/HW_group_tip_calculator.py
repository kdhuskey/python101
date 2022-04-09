def percentage_plus(bill_total, tip_percentage):
    return bill_total + (bill_total * tip_percentage) / 100


def tip_calculator(bill_total, tip_percentage):
    print(f'Your bill total is: ${percentage_plus(bill_total, tip_percentage)}') 


def group_tip_calculator(bill_total, tip_percentage, num_people):
    price_per_people = percentage_plus(bill_total, tip_percentage) / num_people
    total = percentage_plus(bill_total, tip_percentage)
    print(f'The total is {total}')
    print(f'Each person should pay {price_per_people}')


bill_total = int(input('How much was the bill?: '))
tip_percentage = int(input('What percent would you like to tip?: '))   
num_people = int(input('How many people in your party?: '))

group_tip_calculator(bill_total, tip_percentage, num_people)