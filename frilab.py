phonebook = {
'daniels': {'name': 'Chase Daniels', 'phone':'520.275.0004'},
'jones': {'name': 'Chris Jones', 'phone': '503.294.7094'}
}

def pn(dic, name):
    print(phonebook[name]['name'])
    print(phonebook[name]['phone'])

def delete():
    correct_name = True
    while correct_name == True:
        delete_name = input('Enter the last name of the person you wish to delete from the phonebook: ')
        if delete_name in phonebook:
            del phonebook[delete_name]
            correct_name = False
        else:
            print(phonebook)
            print('Name not in phonebook. Try again.')

def add_entry():
    new_name = True
    while new_name == True:
        key_name = input('What is the last name, in lower case, of the person you wish you add?: ')
        full_name = input('What is the first and last name, upper case, of the person you wish to add?:')
        phone = input('What is the phone number of the person you wish to add?: ')
        if key_name not in phonebook:
            phonebook[key_name] = {'name': full_name, 'phone': phone}
            new_name = False
        else:
            print('Name is already in the phonebook: ')

def edit_entry():
    fix_name = True
    while fix_name == True:
        k_name = input('Last name: ')
        n_name = input('Replacement last name: ')
        f_name = input('Replacement First and Last name: ')
        fone = input('Replacement Phone Number: ')
        if k_name in phonebook:
            del phonebook[k_name]
        phonebook[n_name] = {'name': f_name, 'phone': fone}
        fix_name = False


def lookup():
    look_name = input('Enter the last name of the person you are looking for: ')
    if look_name in phonebook:
        pn('name', look_name)
    else:
        print('That name does not exist in this phonebook.')

print('''
Welcome to the phonebook. You can do one of the following:
-> To view the phonebook, enter "V".
-> To edit an entry, enter "E".
-> Look up a name in the phonebook, enter "L".
-> Delete a name in the phonebook, enter "D".
-> Or add a new name to the phonebook, enter "N".
-> To quit the program, enter "Q".''')

# print(phonebook)
# lookup
# delete_name()
# add_entry()


program_running = True

while program_running == True:
    decision = input('What would you like to do?: ')
    if decision == 'V':
        print(phonebook)
    elif decision == 'L':
        lookup()
    elif decision == 'D':
        delete()
    elif decision == 'E':
        edit_entry( )
    elif decision == 'N':
        add_entry()
    elif decision == 'Q':
        quit()
    else:
        print('That\'s not a valid entry. Try again, minion.')
