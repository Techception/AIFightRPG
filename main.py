
import functions
import classes

PLAY = True 

#max values 
MAX_CYCLE = 60
MAX_HEALTH = 16
MAX_ATTACK = 12

p1 = classes.character(MAX_HEALTH)
p2 = classes.character(MAX_HEALTH)
#Main Cylce
cycle = -1
while cycle < MAX_CYCLE: #continue if time remain 
    cycle += 1
    #Status
    countdown = MAX_CYCLE - cycle
    functions.status(countdown, p1, p2)
    if p1.KO or p2.KO: #if a character is KO'd then who won? 
        functions.who_won(p1, p2)
        break
    
    #PLAYER
    #Player 1 and 2 decide on action 
    actionQueue = {
        'p1': p1.attack(cycle),
        'p2': p2.attack(cycle)
    }
    #print("type ", type(actionQueue['p1']))

    #PROCESS
    #Players
    #calculate damage
    reactionQueue = {
        'p1': p1.take_damage(actionQueue['p2']),
        'p2': p2.take_damage(actionQueue['p1'])
    }
        
    
        
    