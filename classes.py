import animations

class character:
    def __init__(self, name:str='nemo', MAX_HEALTH:int=60, speed:int=1) -> None:
        self.KO = False
        self.name = name
        self.health = MAX_HEALTH
        self.actionQueue = []
        
    def __str__(self):
        status = f'{self.name}: {self.health}'
        return status
        
    def act(self):
        action = {'hit':None,'graphic':None}
        #queue the next action if queue is empty 
        if len(self.actionQueue) == 0:
            self.attack_queue()
        #pop off the last item in the queue and action 
        if len(self.actionQueue) > 0:
            action = self.actionQueue.pop()
        return action
        
    def attack_queue(self):
        self.actionQueue += animations.animation_cycle_attack
        
    
        
if __name__ == '__main__':
    import functions
    p1 = character()
    p2 = character()
    
    while (p1.health > 0) and (p2.health > 0):
        functions.calculate_action(p1, p2)
        print(p1,p2)
        
    functions.who_won(p1, p2)

    