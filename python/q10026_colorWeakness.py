import sys

input = sys.stdin.readline
DIR = ((-1, 0), (0, -1), (1, 0), (0, 1))


# Get Input
N = int(input())
pic = []
for i in range(N) :
    pic.append(input().strip())


rootA = [i for i in range(N*N)]
rootB = [i for i in range(N*N)]

def union(x, y, root) :
    x = find(x, root)
    y = find(y, root)

    root[y] = x

def find(x, root) :
    if root[x] == x :
        return x
    else :
        root[x] = find(root[x], root)
        return root[x]

def downDimension(i, j) :
    return i * N + j

for i in range(N) :
    for j in range(N) :
        cur = pic[i][j]
        for dir in DIR :
            dy, dx = dir
            if not (i+dy < 0 or i+dy >= N or j+dx < 0 or j+dx >= N) :
                if pic[i+dy][j+dx] == cur :
                    union(downDimension(i, j), downDimension(i+dy, j+dx), rootA)
                if (pic[i+dy][j+dx] == "B" and cur == "B") or (not (pic[i+dy][j+dx] == "B") and not (cur == "B")) :
                    union(downDimension(i, j), downDimension(i+dy, j+dx), rootB)

for i in range(N*N) :
    find(i, rootA)
    find(i, rootB)

lenA = len(set(rootA))
lenB = len(set(rootB))

print("%d %d"%(lenA, lenB))
# for i in range(N) :
#     for j in range(N) :
#         print(rootA[downDimension(i, j)],end=" ")
#     print("")

# for i in range(N) :
#     for j in range(N) :
#         print(rootB[downDimension(i, j)],end=" ")
#     print("")