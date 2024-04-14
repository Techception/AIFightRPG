import os
import time
import random

clear = lambda: os.system('clear')

neutral = "0  \n|  \n|  \n"

attack_graphic_frame1 = "0  \n|v \n|  \n"
attack_graphic_frame2 = " 0 \n<|-\n | \n"
attack_graphic_frame3 = " 0  \n<|--\n/ 7 \n"

attack_frame = {'hit':None,'graphic':None}
attack_frame1 = {'hit':False,'graphic':attack_graphic_frame1}
attack_frame2 = {'hit':False,'graphic':attack_graphic_frame2}
attack_frame3 = {'hit':True,'graphic':attack_graphic_frame3}

animation_cycle_attack = [attack_frame1, attack_frame2, attack_frame3, attack_frame2, attack_frame1]

def draw(frame:dict):
    clear()
    print(frame['graphic'])
    time.sleep(0.5)
    

if __name__ == "__main__":
    #print(neutral)
    print(attack_frame1['graphic'])
    print(attack_frame2['graphic'])
    print(attack_frame3['graphic'])
    
    frames = animation_cycle_attack[:]
    while True:
        if len(frames) == 0:
            frames = animation_cycle_attack[:]
        else:
            frame = frames.pop()
            draw(frame)