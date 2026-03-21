import random
def calculate_damage(attack, armor):
    dmg = attack - armor
    if dmg <= 0:
        return (0)
    crit = random.randint(0, 3)
    if crit == 1:
        print('Critical hit!')
        return(dmg * 2)
    else:
        return(dmg)

running = True
while running == True:
    print('Welcome to the damage calculator! To stop, write: "stop"')
    temp = input('Attack: ')
    if temp == 'stop':
        break
    try:
        atk = int(temp)
    except:
        print('Error: Bara siffror')
        continue
    temp = input('Armor: ')
    if temp == 'stop':
        break
    try:
        armor = int(temp)
    except:
        print('Error: Bara siffror')
        continue
    print('You did:', calculate_damage(atk, armor),'damage!')