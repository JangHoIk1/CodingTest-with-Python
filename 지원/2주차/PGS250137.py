def solution(bandage, health, attacks):
    h = health
    index = 0
    b = 0
    e  = attacks[-1][0]
    
    for i in range(e + 1):
        if i == attacks[index][0]:
            h -= attacks[index][1]
            b = 0
            index += 1
        else:
            b += 1
            h = min(health, h + bandage[1])
            
            if b == bandage[0]:
                b = 0
                h = min(health, h + bandage[2])
        
        if h <= 0:
            return -1
        
    return h