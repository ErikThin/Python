import random

def dice(quantity, sides = 6):
    """Rolls dice and shows each and total."""
    rolls = []
    for x in range(quantity):
        rolls.append(random.randint(1, sides))
    total = 0
    for y in range(len(rolls)):
        print('Roll %s is %s'%(y+1,rolls[y]))
        total += rolls[y]
    print('Total = %s'%(total))
    print()
    return rolls

if __name__ == '__main__':
    while True:
        dice(int(input('Amount of dice: ')))
        #dice(input('Amount of dice: '), input('Number of sides: '))
