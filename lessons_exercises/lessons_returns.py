def add(a, b):
    print(a + b)
def subtract(a, b):
    print(a - b)
def multiply(a, b):
    print(a * b)
def divide(a, b):
    print(a/b)



def pancake_cal(number_guest, pancakes_per_g):
    total_pan_needed = round(number_guest * pancakes_per_g * .12)
    return number_guest * pancakes_per_g + total_pan_needed

guest_one = int(input('How many would you like?'))
guest_two = int(input('How many would you like?'))    
pancake_total = pancake_cal(guest_one, guest_two)
print(pancake_total)


def fahrenheit_to_celsius(f_temp):
    return(round((f_temp - 32) * 5/9))

whats_the_temp = int(input('What is the temperature outside in Fahrenheit? '))

fah_question = fahrenheit_to_celsius(whats_the_temp)
print(f'Ok, here\'s that temperature in Celsius: {fah_question}')




def celsius_to_fahrenheit(c_temp):
    return round(c_temp * 9/5 + 32)
whats_the_temp_C = int(input('Whats the outside temperature in Celsius? '))
celsius_question = celsius_to_fahrenheit(whats_the_temp_C)
print(f'Ok here\'s the outside temperature in Fahrenheit: {celsius_question}')




# def fuel_price(AU_price, US_price):
#     a_lit = 1.93
#     us_lit = 1.45
#     gal_to_lit = 3.785
#     print(us_lit * gal_to_lit)
# fuel_price(1.93, 1.45)

# def calculate_equity(years_worked, company_valuation):
#     employee_earns = 2500
#     company_shares = 10000000
#     print((employee_earns * years_worked) / ())
# calculate_equity(10, 5) 