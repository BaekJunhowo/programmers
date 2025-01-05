def solution(survey, choices):
    answer = ''
    d = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 
        'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0 }
    
    for choice, quest in zip(choices, survey):
        if choice > 4:
            d[list(quest)[1]] += choice - 4
            
        elif choice < 4:
            d[list(quest)[0]] += 4 - choice
            
    d = list(d.items())
    
    for i in range(0, 8, 2):
        answer += max(d[i:i + 2], key=lambda x: x[1])[0]
    return answer