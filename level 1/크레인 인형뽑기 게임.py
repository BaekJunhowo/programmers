def solution(board, moves):
    answer = 0
    puppets = []
    
    for move in moves:
        col = [row[move - 1] for row in board]
        
        if len(set(col)) == 1:
            continue
        else:
            for i, c in enumerate(col):
                if c == 0:
                    continue
                else:
                    puppets.append(c)
                    board[i][move - 1] = 0
                    if len(puppets) > 1:
                        while puppets[-2] == puppets[-1]:
                            del puppets[-2:]
                            answer += 2
                            if len(puppets) == 1:
                                break
                    break
    return answer

def solution(board, moves):
    answer = 0
    puppets = []
    
    for move in moves:
        col = [row[move - 1] for row in board]
        
        for i, c in enumerate(col):
            if c == 0:
                continue
            else:
                puppets.append(c)
                board[i][move - 1] = 0
                if len(puppets) > 1:
                    while puppets[-2] == puppets[-1]:
                        del puppets[-2:]
                        answer += 2
                        if len(puppets) == 1:
                            break
                break
    return answer

def solution(board, moves):
    answer = 0
    puppets = []

    for move in moves:
        col = [row[move - 1] for row in board]
        
        for i, c in enumerate(col):
            if c == 0:
                continue
            else:
                puppets.append(c)
                board[i][move - 1] = 0
                while len(puppets) > 1 and puppets[-2] == puppets[-1]:
                    del puppets[-2:]
                    answer += 2
                break
    return answer


def solution(board, moves):
    answer = 0
    puppets = []

    for move in moves:
        col = [row[move - 1] for row in board]
        
        for i, c in enumerate(col):
            if c == 0:
                continue
            else:
                puppets.append(c)
                board[i][move - 1] = 0
                if len(puppets) > 1:
                    while puppets[-2] == puppets[-1]:
                        del puppets[-2:]
                        answer += 2
                        if len(puppets) <= 1:
                            break
                break
    return answer