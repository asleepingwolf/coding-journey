import random
import json
from src.common.textrpg.monsters import MonsterClass
from src.common.interface import clear_screen

#Main class for all characters 
class Entity():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Inventory:
    def __init__(self):
        self.items = {}
    def add(self, item_name):
        # .get(item, 0) hämtar nuvarande antal, eller 0 om föremålet inte finns
        current_amount = self.items.get(item_name, 0)
        self.items[item_name] = current_amount + 1
        print(f"Added 1 {item_name} to inventory.")



#Player class, weapons
class PlayerClass(Entity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.weapon = 'Fists'
    def takedamage(self, amount):
        self.health -= amount
        print(f"--> {self.name} tog {amount} i skada! (HP kvar: {self.health})")
    def heavy_attack(self):
        temp = random.randint(0 , 3)
        if temp == 0:
            print("You missed!")
            pass
        else:
            # Räkna ut skadan först
            min_dmg = int(self.damage * 1.75 - 2)
            max_dmg = int(self.damage * 1.75)
            heavy_dmg = random.randint(min_dmg, max_dmg)
            # Skicka in den färdiga siffran
            return(heavy_dmg)




#Initialising the player
player = PlayerClass('Julia', 100 , 5)

print(player.name)
print(player.weapon)
#print(f' Du har: {player.inventory}')

# Väljer ett random monster från monster filen
#enemy_data = random.choice(monsters)

#
#active_enemy = MonsterClass(
#    enemy_data["name"],
#    enemy_data["hp"],
#    enemy_data["dmg"],
#    enemy_data["ability"]
#)
#room = [1]
clear_screen()
print(f'Welcome {player.name}! \n ')
#print(active_enemy.name, active_enemy.ability)
#print(player.inventory)
choice = input(f'You stand in front of a door to a giant fortress. What would you like to do? \n 1. Enter \n 2 Leave \n ')
if int(choice) == 1:
    playing_game = True
else:
    print(f'You go home and live your boring normal life. \n ---GAME OVER!---')
    exit()

print(f"You push open the doors to the fortress and enter. \n")
#Game loop
while playing_game == True:
    fighting = True
    enemy_data = random.choice(monsters)
    active_enemy = MonsterClass(
        enemy_data["name"],
        enemy_data["hp"],
        enemy_data["dmg"],
        enemy_data["ability"]
    )
    print(f"In front of you stands {active_enemy.name} \n")
    while active_enemy.health > 0 and player.health > 0:
        choice = input("\n 1. Normal attack, 2. Hard attack: ")
        try:
            if int(choice) == 1:
                active_enemy.takedamage(random.randint(player.damage -2, player.damage + 2))
            elif int(choice) == 2:
                    active_enemy.takedamage(player.heavy_attack())
            else:
                print("Choices was 1 or 2...")
                continue
        except ValueError:
            print("Error, Choice 1 or 2")
            continue
        player.takedamage(active_enemy.damage)

    exit()
