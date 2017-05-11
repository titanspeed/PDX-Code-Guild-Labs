from weaponnames import w_names
from weaponnames import fa_names
from weaponnames import a_names

class Items:
    def __init__(self, name, type, effect, weight):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect, self.weight)


def weapon():
    return Items(random.choice(w_names), 'weapon', random.randrange(1, 50), random.randrange(5, 50))


def armor():
    return Items(random.choice(a_names), 'armor', random.randrange(1, 50), random.randrange(1, 50))


def first_aid():
    return Items(random.choice(fa_names), 'first aid', random.randrange(5, 100), random.randrange(1, 5))

helmet = armor()
sword = weapon()
potion = first_aid()

print(sword)
print(helmet)
print(potion)
