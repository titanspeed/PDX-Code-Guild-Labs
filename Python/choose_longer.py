# Return the longest.
# >>> choose_longer("Greg", "Rooney")
# 'Rooney'

def choose_longer(name1, name2):
    if len(person1) > len(person2):
        return ('{} is a longer name than {}.'.format(person1, person2))
    elif len(person2) > len(person1):
        return ('{} is a longer name than {}.'.format(person2, person1))
    else:
        return ('Nice try! Those are the same length!')

person1 = input('Enter a name: ')
person2 = input('Enter another name: ')

print(choose_longer(person1, person2))
