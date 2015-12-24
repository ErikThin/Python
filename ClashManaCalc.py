#Clash of Clans profits calculation

TROOPS = {
    "barbarian":['e',[25,40,60,80,100,150,200]],
    "archer":['e',[50,80,120,160,200,300,400]],
    "goblin":['e',[25,40,60,80,100,150]],
    "giant":['e',[250,750,1250,1750,2250,3000,3500]],
    "wall breaker":['e',[1000,1500,2000,2500,3000,3500]],
    "balloon":['e',[2000,2500,3000,3500,4000,4500]],
    "wizard":['e',[1500+500*x for x in range(7)]],
    "healer":['e',[5000,6000,8000,10000]],
    "dragon":['e',[25000,30000,36000,42000]],
    "pekka":['e',[30000,35000,40000,45000,50000]],
    "minion":['d',[6,7,8,9,10,11]],
    "hog rider":['d',[40,45,52,58,65]],
    "valkyrie":['d',[70,100,130,160]],
    "golem":['d',[450,525,600,675,750]],
    "witch":['d',[250,350]],
    "lava hound":['d',[390,450,510]],
    "lightning spell":['s',[15000,16500,18000,20000,22000,24000]],
    "healing spell":['s',[15000,16500,18000,20000,22000,24000]],
    "rage spell":['s',[23000,25000,27000,30000,33000]],
    "jump spell":['s',[23000,27000,31000]],
    "freeze spell":['s',[26000,29000,31000,33000,35000]]
    }

def mana_used(unit, level, quantity):
    return TROOPS[unit][1][level] * quantity

def get_loot_e():
    return int(input("Elixir looted in total? ").replace(',',''))

def get_loot_d():
    return int(input("Dark elixir? ").replace(',',''))

def print_report(report, loot, results):
    print ()
    print (
"""
+------------+
| Units Used |
+------------+
"""
        )
    
    print ("Elixir units")
    if report[0] == []:
        print ("No troops used.")
    for x in report[0]:
        print (str(x).replace(',',' --> '))
    print ()
    
    print ("Dark elixir units")
    if report[1] == []:
        print ("No troops used.")
    for x in report[1]:
        print (str(x).replace(',',' --> '))
    print ()

    print ("Spells")
    if report[2] == []:
        print ("No spells used.")
    for x in report[2]:
        print (str(x).replace(',',' --> '))
    print ()
    print ("Elixir looted: %s"%(loot[0]))
    print ("Elixir Profit: %s"%(results[0]))
    print ("Dark Elixir looted: %s"%(loot[1]))
    print ("Dark Elixir Profit: %s"%(results[1]))

def available_troops():
    print ("Available troops are as follows:")
    troops = "%s. "%(', '.join(TROOPS.keys()))
    if len(troops)>80:
        place = troops.index(',',65)
        troops = troops[:place+1] + '\n' + troops[place+2:]
        if len(troops)>160:
            place = troops.index(',',135)
            troops = troops[:place+1] + '\n' + troops[place+2:]
    print (troops)
    print ('_'*70)
    print ()
    #print ("%s. "%(', '.join(TROOPS.keys())))

while True:
    total_mana_e = 0
    total_mana_d = 0
    report = [[],[],[]] #1.elixir unit, dark unit, spell
    while True:
        available_troops()
        unit = ''
        while unit not in list(TROOPS.keys()):
            unit = input("Troop name? (Without the 's') ").lower()
        level = 0
        while level > len(TROOPS[unit][1]) or level < 1:
            level = int(input("Troop level? Max of %s. "%(len(TROOPS[unit][1]))))
        number = input("How many? ")
        while not number.isnumeric():
            number = input("A number, please... ")
        number = int(number.replace(',',''))
        mana = mana_used(unit, level-1, number) #calculate mana used for that unit
        if TROOPS[unit][0] == 'e': #if it's an elixir troop
            total_mana_e += mana
            report[0].append([unit+' Level '+str(level),mana])
        elif TROOPS[unit][0] == 's':
            total_mana_e += mana
            report[2].append([unit+' Level '+str(level),mana])
        else:                       #else if it's a dark elixir troop
            total_mana_d += mana
            report[1].append([unit+' Level '+str(level),mana])
        if input("Is that all? ").lower().startswith('y'):
            print ()
            break
        print ()
    loot_e = get_loot_e() #elixir
    loot_d = get_loot_d() #dark elixir
    results_e = loot_e - total_mana_e
    results_d = loot_d - total_mana_d
    results = [results_e,results_d]
    loot = [loot_e, loot_d]
    print_report(report,loot,results)
    print ('')
    print ("Do you have another calculation to make?")
    if input().lower().startswith('n'):
        print ()
        break
    print ()
