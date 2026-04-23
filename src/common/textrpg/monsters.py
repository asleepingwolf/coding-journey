import random

class Character():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

class MonsterClass(Character):
    def __init__(self, name, hp, damage, ability):
        super().__init__(name, hp, damage)
        self.ability = ability
        self.sticky = False
    def takedamage(self, amount):
        if self.sticky == True:
            random_sticky = random.int(0,3)
            if random_sticky == 0:
                print(f"You missed because of stickiness \n")
            else:
                self.hp -= amount
                print(f"--> {self.name} tog {amount} i skada! (HP kvar: {self.hp})")
        else:
            self.hp -= amount
            print(f"--> {self.name} tog {amount} i skada! (HP kvar: {self.hp})")
    def Monster_state(self):
        if self.hp > self.hp * 0.5:
            if self.ability == "Sticky":
                self.sticky = True
    def is_alive(self):
        return self.hp > 0



#monsters = [
#    {"name": "Slime", "hp": 40, "dmg": 5, "ability": "Sticky"},
#    {"name": "Rabid Wolf","hp": 50, "dmg": 12, "ability": "Pack Mentality"},
#    {"name": "Shadow Stalker", "hp": 70, "dmg": 25, "ability": "Evasion"}
#]

