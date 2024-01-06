def solution(sizes):
    answer = 0
    
    x = []
    y = []
    
    for i in range(len(sizes)):
        x.append(sizes[i][0])
        y.append(sizes[i][1])
        
    max_len = max(max(x), max(y))
        
    if max_len in x:
        for i in range(len(x)):
            if x[i] < y[i]:
                x[i], y[i] = y[i], x[i]
        answer = max_len * max(y)
            
    elif max_len in y:
        for i in range(len(x)):
            if x[i] > y[i]:
                x[i], y[i] = y[i], x[i]
        answer = max_len * max(x)
    
    return answer