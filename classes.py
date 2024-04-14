import random
import copy

class character:
    #state = {'neutral': True,'attack': False,'defend': False}
    #cooldown = 0
    #KO = False
    MAX_STARTUP = 4
    #attackSequence = ['make fist','throw fist','strike','retract fist','neutral']
    attackSequence = [False, False, True, False, False]
    def __init__(self, name:str='nemo', MAX_HEALTH:int=60, speed:int=1) -> None:
        self.state = {'neutral': True,'attack': False,'defend': False}
        self.cooldown = 0
        self.startup = 0
        self.KO = False
        self.name = name
        self.health = MAX_HEALTH
        self.speed = speed
        #self.actions = [self.attack, self.defend, self.neutral] 
        self.attackFrames = copy.deepcopy(character.attackSequence)
        
    def __str__(self):
        #currentState 
        currentState = [k for k,v in self.state.items() if v]
        status = f'{self.name} {currentState}: {self.health} (HP) {self.cooldown} (CD)'
        return status
        
        
    def attack(self) -> bool:
        if len(self.attackFrames) == 0:
            self.attackFrames = copy.deepcopy(character.attackSequence)
            return False
        else:
            return self.attackFrames.pop()
    
    def act(self, cycle:int, p2:object):
        print(self.attackFrames)
        return self.attack()
        

    def take_damage(self, opponentAction:bool) -> None: 
        #print(opponentAction)
        takeDamage = not(self.state['defend'])
        totalDamage = opponentAction * takeDamage
        self.health -= totalDamage
        self.KO = self.health < 0
        
if __name__ == '__main__':
    print(character.attackSequence)

    