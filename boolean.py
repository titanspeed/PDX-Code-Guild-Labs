name = input('What is your name?: ')
age = int(input('Hello {}: How old are you?: '.format(name)))

if age >= 100:
    print('You should be dead by now!')
elif age == 69:
    print('That is the same age as my dad!')
elif age >= 50:
    print('AARP, anyone?')
else:
    print('Oh wow!')

if age == 31:
    print('Winner winner! You are the same age as I am!')
else:
    print('You are really old!')

if (not name == ""):
    print('Great name, by the way!')
