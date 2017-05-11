class Loot:
    def __init__(self):


class Entity:
    def __init__(self, health, name):
        self.weapon = None
        self.health = 0
        self.location = None
        self.armor = 0
        self.name = name

    def __str__(self):
        return self.name


class Ability:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg


class Monster:
    def __init__(self, health, name):
        Entity.__init__(self, health, name)
        self.ability = None
        self.is_alive = True

    def self generate_loot(self):


class Player(Entity):
    def __init__(self, health, name):
        Entity.__init__(self, health, name)
