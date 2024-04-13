import random

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