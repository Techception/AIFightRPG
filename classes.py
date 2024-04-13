import random

class character:
    #state = {'neutral': True,'attack': False,'defend': False}
    #cooldown = 0
    #KO = False
    def __init__(self, name:str='nemo', MAX_HEALTH:int=60, speed:int=1) -> None:
        self.state = {'neutral': True,'attack': False,'defend': False}
        self.cooldown = 0
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
        for key in self.state:
            self.state[key] = False
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
            self.cooldown = 4
            print(self.name, end=' ')
            print('attack')
            return random.choice([True, False])
        else: 
            print(self.name, end=' ')
            print('no action')
            return False
    
    def act(self, cycle:int, p2:object):
        if self.cooldown == 0:
            action = random.choice(self.actions)
            return action()
        else:
            print(self.name, end=' ')
            print('no action')
        return False
        
    def relax(self):
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
    print(p1)

    