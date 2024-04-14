import random
import copy

class character:
    def __init__(self, name:str='nemo', MAX_HEALTH:int=60, speed:int=1) -> None:
        self.state = {'neutral': True,'attack': False,'defend': False}
        self.cooldown = 0
        self.startup = 0
        self.KO = False
        self.name = name
        self.health = MAX_HEALTH
        self.speed = speed
        self.actionQueue = []
        
    def __str__(self):
        #currentState 
        currentState = [k for k,v in self.state.items() if v]
        status = f'{self.name} {currentState}: {self.health} (HP) {self.cooldown} (CD)'
        return status
        
    #def decide(self):
    #    if len(self.actionQueue) == 0:
    #        self.attack_queue()

    def act(self):
        #queue the next action if queue is empty 
        if len(self.actionQueue) == 0:
            self.attack_queue()
        #pop off the last item in the queue and action 
        if len(self.actionQueue) > 0:
            action = self.actionQueue.pop()
        return action
        
    def attack_queue(self):
        attackDamage = random.choice([True,False])
        attackSequence = [False, False, attackDamage, False, False]
        self.actionQueue += attackSequence
    
        
if __name__ == '__main__':
    print(character.attackSequence)

    