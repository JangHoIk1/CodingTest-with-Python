def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for i, person in enumerate(name):
        score[person] = yearning[i]
    print(score)
    
    for i in photo:
        sum = 0
        for j in i:
            if j in name:
                sum += score[j]
        answer.append(sum)
    
    return answer