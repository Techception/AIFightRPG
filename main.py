MAX_CYCLE = 60
MAX_HEALTH = 16
MAX_ATTACK = 12


p1_alive = True 
p2_alive = True
p1_health = MAX_HEALTH
p2_health = MAX_HEALTH
timer = MAX_CYCLE

p1Vp2 = 0 
p2Vp1 = 0 
stillTime = 1 


PLAY = True 
cycle = 0
#Main Cylce
while PLAY:
    #Status
    print("---")
    print(f'Start Cycle Continue: {PLAY}')
    print(f'Time: {timer}')
    print(f'p1Vp2: {p1Vp2}')
    print(f'p2Vp1: {p2Vp1}')
    print(f'p1_health: {p1_health}')
    print(f'p2_health: {p2_health}')
    
    #PLAYER
    #Player 1 decide
    p1_attack = 1
    p1_defend = 1
    #Player 2 decide
    p2_attack = 1
    p2_defend = 1
    
    #PROCESS
    #Players
    p1Vp2 = p2_defend - p1_attack
    p2Vp1 = p1_defend - p2_attack
    p1_health -= p1Vp2
    p2_health -= p2Vp1
    p1_alive = p1_health > 0 
    p2_alive = p1_health > 0 
    #clock
    cycle += 1
    timer = MAX_CYCLE - cycle
    stillTime = timer >= 0 
    PLAY = (stillTime == p1_alive == p2_alive)
    print(f'End Cycle Continue: {PLAY}')
    