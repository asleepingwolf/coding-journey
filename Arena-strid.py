

class Character():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def takedamage(self, damage):
        self.health = self.health - damage




hero  = Character('Hero', 100, 5)
monster = Character('Frog', 75, 5)
print(hero.name, hero.health)
print(monster.name, monster.health)
while hero.health > 0 and monster.health >0:
    monster.takedamage(hero.damage)
    print('Hero attakcs monster and deals:', hero.damage, 'Monster Health is now:', monster.health)
    hero.takedamage(monster.damage)
    print('Hero Health: ', hero.health)


