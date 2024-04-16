neutral = "0  \n|  \n|  \n"

attack_graphic_frame1 = "0  \n|v \n|  \n"
attack_graphic_frame2 = " 0 \n<|-\n | \n"
attack_graphic_frame3 = " 0  \n<|--\n/ 7 \n"

attack_frame = {'hit':None,'graphic':None}
attack_frame1 = {'hit':False,'graphic':attack_graphic_frame1}
attack_frame2 = {'hit':False,'graphic':attack_graphic_frame2}
attack_frame3 = {'hit':True,'graphic':attack_graphic_frame3}

animation_cycle_attack = [attack_frame1, attack_frame2, attack_frame3, attack_frame2, attack_frame1]


class animation:
    faceRight_neutral = [
        {'hit': None,'graphic': "0  \n|  \n|  \n"}
        ]
        
    faceRight_attack = [
        {'hit': False, 'graphic': "0  \n|v \n|  \n"}, 
        {'hit': False, 'graphic': " 0 \n<|-\n | \n"}, 
        {'hit': True,  'graphic': " 0  \n<|--\n/ 7 \n"},
        {'hit': False, 'graphic': " 0 \n<|-\n | \n"}, 
        {'hit': False, 'graphic': "0  \n|v \n|  \n"}
        ]
        
    faceRight_walk = [
        {'hit': None, 'graphic': " 0 \n<|\ \n | \n"},
        {'hit': None, 'graphic': " 0 \n/|\ \n |7\n"},
        {'hit': None, 'graphic': " 0 \n/|\ \n/ \ \n"}
        ]
    

if __name__ == "__main__":
    import functions
    
    frames = animation()
    n = 0
    while True:
        index = n%3
        frame = frames.faceRight_walk[index]
        n = n + 1 
        functions.draw(frame)