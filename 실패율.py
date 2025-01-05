def solution(N, stages):
    d = {}
    
    for i in range(1, N + 2):
        d[str(i)] = 0
        
    for s in stages:
        d[str(s)] += 1
    
    sum_n = d[str(N + 1)]
    for s in range(N, 0, -1):
        sum_n += d[str(s)]
        d[str(s)] = d[str(s)] / sum_n
    
    d.pop(str(N + 1))
    
    d = sorted(d.items(), key=lambda x : x[1], reverse=True)
    d = [int(x[0]) for x in d]

    return d

def solution(N, stages):
    d = {}
    
    for i in range(1, N + 2):
        d[str(i)] = 0
        
    for s in stages:
        d[str(s)] += 1
    
    sum_n = d[str(N + 1)]
    for s in range(N, 0, -1):
        sum_n += d[str(s)]
        if d[str(s)] == 0:
            d[str(s)] = 0
        else:
            d[str(s)] = d[str(s)] / sum_n
    
    d.pop(str(N + 1))
    
    d = sorted(d.items(), key=lambda x : x[1], reverse=True)
    d = [int(x[0]) for x in d]

    return d