# User Greeter

def say_hello(first_name, last_name):
    print(f'Hello, {first_name} {last_name} welcome to the introduction to functions!')
say_hello('kyle', 'huskey')
say_hello('Lincoln', 'Sawyer')

#Email Generator

def email_gen(first_name, last_name, domain):
    print(f'{first_name[0].lower()}.{last_name.lower()}@{domain.lower()}.com')
email_gen('Kyle', 'Huskey', 'SpOtIFY')
email_gen('batman', 'superhero', 'GoThamcity')

#Username Generator

def username(first_name, last_name):
    print(f'{first_name[0:3].lower()}_{last_name[0:5].lower()}')
username('Kyle', 'huskey')
username('Batman', 'isbstyouknow')

# New User Contact Info

def new_user_card(first_name, last_name, domain):
    say_hello(first_name, last_name)
    email_gen(first_name, last_name, domain)
    username(first_name, last_name)
new_user_card('kyle', 'huskey', 'spotify')

#new_user_card('Batman', 'the best super hero', 'Gotham')