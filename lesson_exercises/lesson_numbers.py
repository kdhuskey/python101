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
    print(number_guest * pancakes_per_g + total_pan_needed)
pancake_cal(10, 3)
pancake_cal(5, 3)


def fahrenheit_to_celsius(f_temp):
    print(round((f_temp - 32) * 5/9))
#print(fahrenheit_to_celsius(100))
fahrenheit_to_celsius(212)

def celsius_to_fahrenheit(c_temp):
    print(round(c_temp * 9/5 + 32))
celsius_to_fahrenheit(100)

def fuel_price(AU_price, US_price):
    a_lit = 1.93
    us_lit = 1.45
    gal_to_lit = 3.785
    print(us_lit * gal_to_lit)
fuel_price(1.93, 1.45)

def calculate_equity(years_worked, company_valuation):
    employee_earns = 2500
    company_shares = 10000000
    print((employee_earns * years_worked) / ())
calculate_equity(10, 5) 