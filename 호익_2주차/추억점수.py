def solution(name, yearning, photo):
    answer = []
    sum = 0
    cnt =0
    
    for j in range(len(photo)):
        for i in range(len(name)):
            
            if name[i] in photo[j]:
                sum+=yearning[i]
        
        
        answer.append(sum)
        sum=0
    
            
    
    return answer


