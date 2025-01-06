def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    
    d = {}
    for user in id_list:
        d[user] = [0, []]

    for rep in report:
        d[rep.split()[1]][0] += 1
        d[rep.split()[0]][1].append(rep.split()[1])
        
    for user in id_list:
        n = 0
        for u in d[user][1]:
            if d[u][0] >= k:
                n += 1
                
        answer.append(n)
    return answer

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer