noun = input('Please enter a noun: ')
present_verb = input('Please enter a present-tense verb: ')
name = input('Please enter a name: ')

def madlib(noun, verb, name):
    print(f"""There once was a {noun} that suddenly came to life, called themselves {name} and starting {verb} around the town.
{name} decided that {verb} was un acceptable and decided to move to the countryside ond live a life of solitude.""")
madlib(noun, present_verb, name)
