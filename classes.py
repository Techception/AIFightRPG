import animations

class character:
    def __init__(self, name:str='nemo', MAX_HEALTH:int=60, speed:int=1) -> None:
        self.KO = False
        self.name = name
        self.health = MAX_HEALTH
        self.actionQueue = []
        

    def act(self):
        #queue the next action if queue is empty 
        if len(self.actionQueue) == 0:
            self.attack_queue()
        #pop off the last item in the queue and action 
        if len(self.actionQueue) > 0:
            action = self.actionQueue.pop()
            animations.draw(action)
        return action
        
    def attack_queue(self):
        self.actionQueue += animations.animation_cycle_attack
    
        
if __name__ == '__main__':
    p1 = character()
    
    while True:
        p1.act()

    