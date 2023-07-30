import sys
input = sys.stdin.readline
DIR = ((0, -1), (1, 0), (0, 1), (-1, 0))
R, C, T = map(int, input().split(" "))

field = []
purifier = -1

# get field input
for i in range(R):
    field.append(list(map(int, input().split(" "))))
    if purifier == -1 and field[-1][0] == -1 :
        purifier = i

def isValid(row, col) :
    if row >= 0 and row < R and col >= 0 and col < C and field[row][col] != -1 :
        return True
    else :
        return False

for t in range(T) :
    # diffusion
    field2 = [[0 for i in range(C)] for j in range(R)]
    field2[purifier][0], field2[purifier+1][0] = -1, -1
    for row in range(R) :
        for col in range(C) :
            if field[row][col] != 0 and field[row][col] != -1 :
                count = 0
                for dy, dx in DIR :
                    if isValid(row+dy, col+dx):
                        count += 1
                        field2[row+dy][col+dx] += int(field[row][col] / 5)
                field2[row][col] += field[row][col] - int(field[row][col] / 5) * count


    # purifying - upper
    pre = 0
    for col in range(1, C) :
        pre, field2[purifier][col] = field2[purifier][col], pre

    for row in reversed(range(purifier)) :
        pre, field2[row][C-1] = field2[row][C-1], pre
    
    for col in reversed(range(C-1)) :
        pre, field2[0][col] = field2[0][col], pre
    
    for row in range(1, purifier) :
        pre, field2[row][0] = field2[row][0], pre
    
    # purifying - down
    pre = 0
    for col in range(1, C) :
        pre, field2[purifier+1][col] = field2[purifier+1][col], pre

    for row in range(purifier+2, R) :
        pre, field2[row][C-1] = field2[row][C-1], pre
    
    for col in reversed(range(C-1)) :
        pre, field2[R-1][col] = field2[R-1][col], pre
    
    for row in reversed(range(purifier+2, R-1)) :
        pre, field2[row][0] = field2[row][0], pre

    field = field2

dustSum = 0
for row in range(R) :
    for col in range(C) :
        if field[row][col] != -1 :
            dustSum += field[row][col]

print(dustSum)