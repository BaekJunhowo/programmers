def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2],
             '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    
    lpos, rpos = keypad['*'], keypad['#']
    
    for number in numbers:
        if number in [1, 4, 7]:
            lpos = keypad[number]
            answer += 'L'
            
        elif number in [3, 6, 9]:
            rpos = keypad[number]
            answer += 'R'
            
        else:
            n_pos = keypad[number]
            
            l_dist = abs(lpos[0] - n_pos[0]) + abs(lpos[1] - n_pos[1])
            r_dist = abs(rpos[0] - n_pos[0]) + abs(rpos[1] - n_pos[1])
            
            if l_dist < r_dist:
                lpos = n_pos
                answer += 'L'
                
            elif l_dist > r_dist:
                rpos = n_pos
                answer += 'R'
                
            else:
                if hand == 'left':
                    lpos = n_pos
                    answer += 'L'
                else:
                    rpos = n_pos
                    answer += 'R'
            
    return answer