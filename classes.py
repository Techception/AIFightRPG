import random

class character:
    #state = {'neutral': True,'attack': False,'defend': False}
    #cooldown = 0
    #KO = False
    MAX_STARTUP = 4
    def __init__(self, name:str='nemo', MAX_HEALTH:int=60, speed:int=1) -> None:
        self.state = {'neutral': True,'attack': False,'defend': False}
        self.cooldown = 0
        self.startup = 0
        self.KO = False
        self.name = name
        self.health = MAX_HEALTH
        self.speed = speed
        self.actions = [self.attack, self.defend, self.neutral] 
        
    def __str__(self):
        #currentState 
        currentState = [k for k,v in self.state.items() if v]
        status = f'{self.name} {currentState}: {self.health} (HP) {self.cooldown} (CD)'
        return status
        
    def changeState(self, state:str) -> None:
        self.state = {'neutral': False,'attack': False,'defend': False}
        self.state[state] = True
        
    def neutral(self) -> bool:
        self.changeState('neutral')
        self.cooldown = 1
        print(self.name, end=' ')
        print('neutral')
        return False
        
    def defend(self) -> bool:
        neutralStance = self.state['neutral']
        if neutralStance:
            self.changeState('defend')
            self.cooldown = 2
            print(self.name, end=' ')
            print('defend')
        else: 
            print(self.name, end=' ')
            print('no action')
        return False
        
    def attack(self) -> bool:
        neutralStance = self.state['neutral']
        if neutralStance:
            self.changeState('attack')
            self.startup = self.MAX_STARTUP
            self.cooldown = 4
            print(self.name, end=' ')
            print('attacking')
        else: 
            print(self.name, end=' ')
            print('no action')
        return False
            
    def attack_action(self):
        hit = False
        if self.startup == 0:
            hit = random.choice([True, False])
            self.startup = 0
            print(self.name, end=' ')
            print('struk')
        else: 
            self.striking()
        return hit
    
    def act(self, cycle:int, p2:object):
        attackStance = self.state['attack']
        if attackStance:
            return self.attack_action()
        if self.cooldown == 0:
            action = random.choice(self.actions)
            return action()
        else:
            print(self.name, end=' ')
            print('no action')
        return False
        
    def relax(self):
        print(self.name, end=' ')
        print(f'cool down Frames remaining {self.cooldown}')
        if self.cooldown > 0:
            self.cooldown = self.cooldown - 1
    def striking(self):
        print(self.name, end=' ')
        print(f'start up Frames remaining {self.cooldown}')
        if self.startup > 0:
            self.startup = self.startup - 1

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
    print(p1)

    