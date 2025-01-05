def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for l in reserve:
        if l in lost:
            lost.remove(l)
            reserve.remove(l)
            
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
            
    return n - len(lost)

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for l in reserve.copy():
        if l in lost:
            lost.remove(l)
            reserve.remove(l)
            
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
            
    return n - len(lost)