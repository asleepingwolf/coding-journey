import random

class Character():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def takedamage(self, damage_amount):
        self.health -= damage_amount
        print(f"{self.name} took {damage_amount} damage! and has {self.health} hp left")

class Monster(Character):
    def __init__(self, name, health, damage, rage_threshold):
        super().__init__(name, health, damage)
        self.rage_threshold = rage_threshold
        self.status = 'Normal'
    def monster_state(self):
        if self.health <= self.rage_threshold and self.status == 'Normal':
            self.status = 'Angry'
            self.damage *= 2
            print('You made me angry!')
    
class Hero(Character):
    def __init__(self, name, health, damage, weapon):
        super().__init__(name, health, damage)
        self.weapon = weapon
        self.inventory = []
    def inventory_add(self,item):
        self.inventory.append(item)
    def player_weapon(self, newweapon):
        self.weapon = newweapon
        print(f"You equipped {newweapon}!")


player = Hero('Player', 100, 7, 'Fists')
player.player_weapon('Fists')
print(f"Welcome {player.name}! You have {player.health} HP.", f"Your weapon is: {player.weapon}")
monster = Monster('Frog', 75, 5, 40)
print(f"Watch out for: {monster.name}! Den har {monster.health} HP.\n")

while player.health > 0 and monster.health > 0:
    choice = input("\n 1. Normal attack, 2. Hard attack: ")
    try:
        if int(choice) == 1:
            monster.takedamage(random.randint(player.damage -2, player.damage + 2))
        elif int(choice) == 2:
            temp = random.randint(0 , 3)
            if temp == 0:
                print("You missed!")
                pass
            else:
                # Räkna ut skadan först
                min_dmg = int(player.damage * 1.75 - 2)
                max_dmg = int(player.damage * 1.75)
                heavy_dmg = random.randint(min_dmg, max_dmg)
        
                 # Skicka in den färdiga siffran
                monster.takedamage(heavy_dmg)
        else:
            print("Choices was 1 or 2...")
            continue
    except ValueError:
        print("Error, Choice 1 or 2")
        continue
    if monster.health <= 0:
        reward = random.randint(0,2)
        if reward == 0:
            print("you found nothing")
        elif reward == 1:
            print("You found a health potion")
            player.inventory_add('Health potion')
        elif reward == 2:
            print('You found a steel sword')
            player.player_weapon('Steel_sword')
        break
    monster.monster_state()
    player.takedamage(monster.damage)
if player.health > 0:
    print("You Won!")
else:
    print("You Lost!")