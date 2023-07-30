import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
space = []

cctv = []
cctv5 = []
for i in range(N) :
    space.append(list(map(int, input().split(" "))))
    for j in range(M) :
        if space[i][j] == 5 :
            cctv5.append((i, j))
        elif space[i][j] >= 1 and space[i][j] <= 4 :
            cctv.append((i, j, space[i][j]))
        
L = 0
U = 1
R = 2
D = 3

CASES = [
    [],
    [[L], [U], [R], [D]],
    [[L, R], [U, D]],
    [[U, R], [R, D], [D, L], [L, U]],
    [[L, U, R], [U, R, D], [R, D, L], [D, L, U]]
]

def fillSpace(y, x, dir) :
    replaced = []

    if dir == L :
        for nextX in reversed(range(0, x)) :
            if space[y][nextX] == 6 :
                break
            replaced.append(space[y][nextX])
            space[y][nextX] = '#'

    elif dir == R :
        for nextX in range(x+1, M) :
            if space[y][nextX] == 6 :
                break
            replaced.append(space[y][nextX])
            space[y][nextX] = '#'

    elif dir == U :
        for nextY in reversed(range(0, y)) :
            if space[nextY][x] == 6 :
                break
            replaced.append(space[nextY][x])
            space[nextY][x] = '#'

    elif dir == D :
        for nextY in range(y+1, N) :
            if space[nextY][x] == 6 :
                break
            replaced.append(space[nextY][x])
            space[nextY][x] = '#'
    
    return replaced

def recoverSpace(y, x, dir, replaced) :
    if dir == L :
        for i in range(len(replaced)) :
            space[y][x - i - 1] = replaced[i]
    elif dir == R :
        for i in range(len(replaced)) :
            space[y][x + i + 1] = replaced[i]
    elif dir == U :
        for i in range(len(replaced)) :
            space[y - i - 1][x] = replaced[i]
    elif dir == D :
        for i in range(len(replaced)) :
            space[y + i + 1][x] = replaced[i]

def fillSpaces(y, x, dirList) :
    replaces = []
    for dir in dirList :
        replaced = fillSpace(y, x, dir)
        replaces.append(replaced)
    
    return replaces

def recoverSpaces(y, x, dirList, replaced) :
    for i in range(len(dirList)) :
        recoverSpace(y, x, dirList[i], replaced[i])

# No.5
for y, x in cctv5 :
    for i in range(4) :
        fillSpace(y, x, i)

def backtracking(i, cctv) :
    if i >= len(cctv):
        result = 0
        for i in range(N) :
            result += space[i].count(0)
        return result
    
    y, x, kind = cctv[i]

    result = 1e9

    for thisCase in CASES[kind] :
        replaced = fillSpaces(y, x, thisCase)
        result = min(result, backtracking(i+1, cctv))
        recoverSpaces(y, x, thisCase, replaced)
    return result

result = backtracking(0, cctv)
print(result)