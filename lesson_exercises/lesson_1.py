# User Greeter

firstname = 'Kyle'
lastname = 'Huskey'
full_name = 'Kyle Huskey'
print(f'Hello and welcome to DigitalCrafts {full_name}!')

#Email Generator

email = (f'{firstname[0].lower()}.{lastname.lower()}@spotify.com ')
print(email)

#Username Generator

username = (f'{firstname[0:3].lower()}_{lastname[0:5].lower()}')
print(username)

#New User Contact Information

contact_card = (f'Welcome to Spotify, {firstname} {lastname}! \nEmail: {email} \nUsername: {username}')


print(contact_card)