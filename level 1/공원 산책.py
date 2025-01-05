def solution(park, routes):
    park = [list(row) for row in park]
    moves = {'E': [0, 1], 'S': [1, 0], 'W': [0, -1], 'N': [-1, 0]}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                pos = [i, j]

    for route in routes:
        i = int(route.split(' ')[1])
        can_move = True
        pos_b = [pos[0], pos[1]]
        
        for _ in range(i):
            xpos = moves[route.split(' ')[0]][0]
            ypos = moves[route.split(' ')[0]][1]

            if pos_b[0] + xpos >= len(park) or pos_b[1] + ypos >= len(park[0]):
                can_move = False
                break
            elif park[pos_b[0] + xpos][pos_b[1] + ypos] == 'X':
                can_move = False
                break
                
            pos_b[0] += xpos
            pos_b[1] += ypos
                
        if can_move:
            pos = pos_b

    return pos

def solution(park, routes):
    park = [list(row) for row in park]
    moves = {'E': [0, 1], 'S': [1, 0], 'W': [0, -1], 'N': [-1, 0]}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                pos = [i, j]

    for route in routes:
        i = int(route.split(' ')[1])
        can_move = True
        pos_b = [pos[0], pos[1]]
        
        for _ in range(i):
            xpos = moves[route.split(' ')[0]][0]
            ypos = moves[route.split(' ')[0]][1]
            
            nx = pos_b[0] + xpos
            ny = pos_b[1] + ypos

            if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
                can_move = False
                break
                
            elif park[nx][ny] == 'X':
                can_move = False
                break
                
            pos_b[0] += xpos
            pos_b[1] += ypos
                
        if can_move:
            pos = pos_b

    return pos