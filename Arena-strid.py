import random

class Character():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def takedamage(self, damage_amount):
        self.health -= self.health - damage_amount

class Monster(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
    
class Hero(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.inventory = []
    def inventory_add(self,item):
        self.inventory.append(item)



player = Hero('Spelare', 100, 7)
player.inventory_add('Fists')
print(f"Välkommen {player.name}! Du har {player.health} HP.", f"Ditt vapen är: {player.inventory}")
monster = Monster('Frog', 75, 5)
print(f"Akta dig för: {monster.name}! Den har {monster.health} HP.")
#Hero.attack(monster.name)
print(f"Akta dig för: {monster.name}! Den har {monster.health} HP.")

#print(Hero.name, Hero.health)
#print(monster.name, monster.health)
#while hero.health > 0 and monster.health >0:
#    monster.takedamage(hero.damage)
#    print('Hero attakcs monster and deals:', hero.damage, 'Monster Health is now:', monster.health)
#    hero.takedamage(monster.damage)
#    print('Hero Health: ', hero.health)


