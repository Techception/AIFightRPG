import os
import time


def status(countdown:int, p1:object, p2:object) -> None:
    print("---")
    #print(f'Start Cycle Continue: {PLAY}')
    print(f'Time: {countdown}')
    print(f'p1_health: {p1.health}')
    print(f'p2_health: {p2.health}')


def who_won(p1:object, p2:object):
    if p1.KO and p2.KO:
        print('draw game')
    elif p2.KO:
        print('Player 1 wins')
    elif p1.KO:
        print('player 2 wins')
  
clear = lambda: os.system('clear')      
def draw(frame:dict):
    clear()
    print(frame['graphic'])
    time.sleep(0.5)
    
def calculate_action(p1:object, p2:object):
    p1_action = p1.act()
    p2_action = p2.act()
    p1.health = p1.health - p2_action['hit']
    p2.health = p2.health - p1_action['hit']
    p1.KO = p1.health <= 0
    p2.KO = p2.health <= 0
    draw(p1_action)