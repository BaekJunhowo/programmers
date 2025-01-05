def solution(s):
    answer = 0
    while s:
        if len(s) == 1:
            return answer + 1
        
        x = s[0]
        cnt_x, cnt_c = 1, 0
        is_updated = False
        
        for c in s[1:]:
            if x == c:
                cnt_x += 1
            else:
                cnt_c += 1
                
            if cnt_x == cnt_c:
                s = s[cnt_x + cnt_c:]
                answer += 1
                is_updated = True
                break
                
        if not is_updated:
            break
    return answer

def solution(s):
    answer = 0
    while s:
        if len(s) == 1:
            return answer + 1
        
        x = s[0]
        cnt_x, cnt_c = 1, 0
        split_index = -1
        
        for i, c in enumerate(s[1:], start=1):
            if x == c:
                cnt_x += 1
            else:
                cnt_c += 1
            
            if cnt_x == cnt_c:
                split_index = i + 1
                answer += 1
                break
        
        if split_index == -1:
            return answer + 1
        
        s = s[split_index:]
    
    return answer