def capture(matrix):
    """Takes matrix of lists about network. Gives time to overcome network."""
    mat = list(matrix)
    counter = 0
    
    while any(mat[r][r]!=0 for r in range(len(matrix))):
        ls = []
        for x in range(len(matrix)):
            if mat[x][x] == 0:
                for y in range(len(matrix)):
                    if not x==y and mat[x][y] == 1 and y not in ls and not mat[y][y]==0:
                        ls.append(y)
        for t in ls:
            mat[t][t]-=1
        counter += 1
    return counter
