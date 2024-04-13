import random

PLAY = True 

#max values 
MAX_CYCLE = 60
MAX_HEALTH = 16
MAX_ATTACK = 12

#initial player 
class character:
    def __init__(self, MAX_HEALTH:int=60, speed:int=1) -> None:
        self.health = MAX_HEALTH
        self.KO = False
        self.speed = speed
        
    def attack(self,cycle) -> bool:
        turn = cycle % self.speed == 0
        if turn:
            return random.choice([True, False])
        else: 
            return False
            
    def take_damage(self, opponentAction:bool) -> None: 
        self.health -= opponentAction
        self.KO = self.health < 0

def status():
    print("---")
    #print(f'Start Cycle Continue: {PLAY}')
    print(f'Time: {MAX_CYCLE - cycle}')
    print(f'p1_health: {p1.health}')
    print(f'p2_health: {p2.health}')
    
def who_won(p1:object, p2:object):
    if p1.KO and p2.KO:
        print('draw game')
    elif p2.KO:
        print('Player 1 wins')
    elif p1.KO:
        print('player 2 wins')
        
        
########################################################
p1 = character(MAX_HEALTH)
p2 = character(MAX_HEALTH)
#Main Cylce
cycle = -1
while cycle < MAX_CYCLE: #continue if time remain 
    cycle += 1
    
    #Status
    status()
    if p1.KO or p2.KO: #if a character is KO'd then who won? 
        who_won(p1, p2)
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
        
    
        
    