def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch in ['-', '_', '.']:
            answer += ch
            
    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == '.' and len(answer) > 1:
	    answer = answer[1:]
    if answer[-1] == '.':
	    answer = answer[:-1]
    
    if answer == '':
        answer = 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
            
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer