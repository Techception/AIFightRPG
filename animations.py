import os
import time 

clear = lambda: os.system('clear')

neutral = "0  \n|  \n|  \n"

attack_frame1 = "0  \n|v \n|  \n"
attack_frame2 = " 0 \n<|-\n | \n"
attack_frame3 = "0  \n|--\n|  \n"

print(neutral)
print(attack_frame1)
print(attack_frame2)
print(attack_frame3)

cycle = [neutral, attack_frame1, attack_frame2, attack_frame3, attack_frame2, attack_frame1, neutral]


frames = cycle[:]
while True:
    clear()
    if len(frames) == 0:
        frames = cycle[:]
    else:
        frame = frames.pop()
        print(frame)
        time.sleep(1)