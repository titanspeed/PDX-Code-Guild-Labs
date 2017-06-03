lst = []

name = input('Hi, what is your name?: ')

lst.append(name)

name2 = input('And what is your name?: ')

lst.append(name2)

name3 = input('Last but not least, what is your name?: ')

lst.append(name3)

print(lst)

lst2 = []

for thing in range(len(lst)):
    if lst[thing] != "John":
        lst2.append(lst[thing])
lst = lst2

for thing in lst:
    print('Hello {}!'.format(thing))

lst.reverse()
print(lst)

lst.clear()

print(lst)

def bartledoo(thing):
    if lst[thing] == "Chase":
        return ("GREAT!")
    return ("NO!")

bartledoo(0)
