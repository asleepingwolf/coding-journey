import random

#Main class for all characters 
class Character():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

#Player class, weapons inventory
class PlayerClass(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.weapon = 'Fists'
        self.inventory = {}
    def InventoryAdd(self, item):
        # .get(item, 0) hämtar nuvarande antal, eller 0 om föremålet inte finns
        current_amount = self.inventory.get(item, 0)
        self.inventory[item] = current_amount + 1
        print(f"Added 1 {item} to inventory.")

#Monster Class
class MonsterClass(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class RoomClass():
    def __init__(self, luck):
        self.luck = luck
    def RoomMob(self, mob):
        
        MonsterClass()
    def loot(self):
        if self.luck >= 4:
            #temp = random.randint(0,3)
            temp = 0
            if temp == 0:
                player.InventoryAdd('Health Potion')

#Initialising the player
player = PlayerClass('Julia', 100 , 5)

monsters = [
    {"name": "Slime", "hp": 40, "dmg": 5, "ability": "Sticky"},
    {"name": "Shadow Stalker", "hp": 70, "dmg": 25, "ability": "Evasion"},
    {"name": "Rabid Wolf": 50, "dmg": 12, "ability": "Pack Mentality"}
]

print(player.name)
print(player.weapon)
print(f' Du har: {player.inventory}')



room = [1]
room[0] = RoomClass(5)
print(f'Welcome {player.name}! \n ')
print(player.inventory)
choice = input(f'You stand in front of a door to a giant fortress. What would you like to do? \n 1. Enter \n 2 Leave \n ')
if int(choice) == 1:
    playing = True
else:
    print(f'You go home and live your boring normal life. \n ---GAME OVER!---')
    exit()
#Game loop
while playing == True:
    
    exit()
