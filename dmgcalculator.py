import random
def calculate_damage(attack, armor):
    crit = random.randint(0, 1)
    if crit == 1:
        print('Critical hit! Damage done:', (attack - armor) * 2)
    else:
        print('Damage done:', attack - armor)

running = True
while running == True:
    print('Welcome to the damage calculator! För att avsluta skriv "stop"')
    temp = input('Attack: ')
    if temp == 'stop':
        break
    try:
        atk = int(temp)
    except:
        print('Error: Bara siffror')
    temp = input('Armor: ')
    if temp == 'stop':
        break
    try:
        armor = int(temp)
    except:
        print('Error: Bara siffror')
    calculate_damage(atk, armor)