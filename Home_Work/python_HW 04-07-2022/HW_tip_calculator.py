
def percentage_plus(bill_total, tip_percentage):
    return bill_total * (tip_percentage/100) + bill_total


def tip_calculator(bill_total, tip_percentage):
    print(f'Your bill total is: ${percentage_plus(bill_total, tip_percentage)}') 

bill_total = int(input('How much was the bill?: '))
tip_percentage = int(input('What percent would you like to tip?: '))   
    



tip_calculator(bill_total, tip_percentage)


