import sys

# a : tuple of a's coordinate (y, x)
# b : tuple of b's coordinate (y, x)
# dir : next move (y, x)
# count : count of moving
def DFS(a, b, dir, count) :
    if count > 10 :
        return FAIL_CODE
    
    next_a = (a[0] + dir[0], a[1] + dir[1])
    next_b = (b[0] + dir[0], b[1] + dir[1])

    a_out = False
    b_out = False
    
    if next_a[0] < 0 or next_a[0] >= N or next_a[1] < 0 or next_a[1] >= M :
        a_out = True
    if next_b[0] < 0 or next_b[0] >= N or next_b[1] < 0 or next_b[1] >= M :
        b_out = True

    if (a_out and not b_out) or (not a_out and b_out) :
        return count
    
    if a_out and b_out :
        return FAIL_CODE

    if board[next_a[0]][next_a[1]] == '#' :
        next_a = a
    if board[next_b[0]][next_b[1]] == '#' :
        next_b = b    
    
    log = FAIL_CODE
    for i in _dir_ :
        curLog = DFS(next_a, next_b, i, count + 1)
        log = min(log, curLog)            

    return log


_dir_ = ((-1, 0), (0, -1), (1, 0), (0, 1))
FAIL_CODE = 100
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

a = -1
b = -1

for i in range(N) :
    board.append(input().strip())

    o_idx = board[i].find('o')
    if o_idx != -1 : # there is coin in this line
        if a == -1 :
            a = (i, o_idx)
        else :
            b = (i, o_idx)
        
        if board[i].count('o') == 2 : # there are two coin in this line
            b = (i, board[i][o_idx + 1 :].find('o') + o_idx + 1)

answer = DFS(a, b, (0, 0), 0)
if answer == FAIL_CODE :
    answer = -1
print(answer)