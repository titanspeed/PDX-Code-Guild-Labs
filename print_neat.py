def pretty_print(str):
    phonum = str
    phonum1 = list(phonum)
    phonum1.insert(0, '(')
    phonum1.insert(4, ')')
    phonum1.insert(5, ' ')
    phonum1.insert(-4, '-')
    phonum2 = ''.join(phonum1)
    print(phonum2)


pretty_print(input('What phone number?: '))