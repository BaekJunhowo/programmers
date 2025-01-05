def solution(cards1, cards2, goal):
    answer = []
    
    for i in range(len(goal)):
        if goal[i] in cards1 and cards1.index(goal[i]) == 0:
            answer.append(goal[i])
            cards1.remove(goal[i])
            
        if goal[i] in cards2 and cards2.index(goal[i]) == 0:
            answer.append(goal[i])
            cards2.remove(goal[i])

    return 'Yes' if answer == goal else 'No'