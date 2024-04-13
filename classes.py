import random

class character:
    state = {'neutral': True,'attack': False,'defend': False}
    cooldown = 0
    KO = False
    def __init__(self, MAX_HEALTH:int=60, speed:int=1) -> None:
        self.health = MAX_HEALTH
        self.speed = speed
        self.actions = [self.attack, self.defend, self.relax] 
        
    def changeState(self, state:str) -> None:
        for key in self.state:
            self.state[key] = False
        self.state[state] = True
        
    def relax(self) -> None:
        self.changeState('neutral')
        
    def defend(self) -> None:
        neutralStance = self.state['neutral']
        if neutralStance:
            self.changeState('defend')
            self.cooldown = 10
        
    def attack(self) -> bool:
        neutralStance = self.state['neutral']
        if neutralStance:
            self.changeState('attack')
            self.cooldown = 10
            return random.choice([True, False])
        else: 
            return False
    
    def act(self, cycle:int, p2:object):
        print('cool down:',self.cooldown)
        if self.cooldown == 0:
            self.relax()
            action = random.choice(self.actions)
            action()
        if self.cooldown > 0:
            self.cooldown = self.cooldown - 1
            
    def take_damage(self, opponentAction:bool) -> None: 
        #print(opponentAction)
        takeDamage = not(self.state['defend'])
        totalDamage = opponentAction * takeDamage
        self.health -= totalDamage
        self.KO = self.health < 0
        
if __name__ == '__main__':
    cycle = 1
    p1 = character()
    p2 = character()
    p1.act(1,p2)
    print(p1.state)
    p1.act(1,p2)
    print(p1.state)
    p1.act(1,p2)
    print(p1.state)
    