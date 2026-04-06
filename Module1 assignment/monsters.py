import random

class Character():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class MonsterClass(Character):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.ability = ability
        self.sticky = False
    def takedamage(self, amount):
        if self.sticky == True:
            random_sticky = random.int(0,3)
            if random_sticky == 0:
                print(f"You missed because of stickiness \n")
            else:
                self.health -= amount
                print(f"--> {self.name} tog {amount} i skada! (HP kvar: {self.health})")
        else:
            self.health -= amount
            print(f"--> {self.name} tog {amount} i skada! (HP kvar: {self.health})")
    def Monster_state(self):
        if self.health > self.health * 0.5:
            if self.ability == "Sticky":
                self.sticky = True


monsters = [
    {"name": "Slime", "hp": 40, "dmg": 5, "ability": "Sticky"},
    {"name": "Rabid Wolf","hp": 50, "dmg": 12, "ability": "Pack Mentality"},
    {"name": "Shadow Stalker", "hp": 70, "dmg": 25, "ability": "Evasion"}
]

