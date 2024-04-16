
import functions
import classes

PLAY = True 

#max values 
MAX_CYCLE = 60
MAX_HEALTH = 3
MAX_ATTACK = 12

p1 = classes.character('Alex', MAX_HEALTH)
p2 = classes.character('CPU', MAX_HEALTH)
#Main Cylce
cycle = -1
while cycle < MAX_CYCLE: #continue if time remain 
    cycle += 1
    #Status
    countdown = MAX_CYCLE - cycle
    #functions.status(countdown, p1, p2)
    print('----------------')
    print(f'Time: {countdown}')
    print(p1)
    print(p2)
    if p1.KO or p2.KO: #if a character is KO'd then who won? 
        functions.who_won(p1, p2)
        break

    p1.act()



    
        
    