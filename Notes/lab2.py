name = input('Hey, what is your name?: ')

age = int(input('Nice to meet you, {}. How old are you: '.format(name)))

print('''
Wow, {}, you will be {} in one year!
'''.format(name, age + 1))

print('{}{}{}{}{}'.format(name, age, name, age + 1, age + 10))
