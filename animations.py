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
        {'hit': None, 'graphic': "{offset} 0 \n{offset}<|\ \n{offset} | \n{offset}"},
        {'hit': None, 'graphic': "{offset} 0 \n{offset}/|\ \n{offset} |7\n{offset}"},
        {'hit': None, 'graphic': "{offset} 0 \n{offset}/|\ \n{offset}/ \ \n{offset}"}
        ]
    
    def walk(self,vector:int=0):
        import functions
        import copy
        n = 0
        offset = 0
        while vector > 0:
            offset = offset + 1
            move = f" "*offset
            index = n%3
            #print(move)
            
            frame = copy.deepcopy(self.faceRight_walk)
            frame = frame[index]
            frame["graphic"] = frame["graphic"].replace("{offset}",move)
            functions.draw(frame)
            #print(frame["graphic"])
            
            n = n + 1
            vector = vector - 1 
            
    def __init__(self):
        pass 

if __name__ == "__main__":
    frames = animation()
    frames.walk(100)