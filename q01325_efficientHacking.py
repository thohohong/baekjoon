import sys
sys.setrecursionlimit(10**6)

def find(a, visit) :
    cycleFlag = False
    if check[a] :
        return computers[a]
    visit[a] = True
    for i in computers[a] :
        if visit[i] :
            cycleFlag = True
            continue
        computers[a] = computers[a].union(find(i, visit))
    if not cycleFlag :
        check[a] = True
    return computers[a]

input_ = input("").split()

N = int(input_[0])
M = int(input_[1])

computers = list(set() for i in range(N + 1))
check = list(False for i in range(N + 1))

for i in range(N + 1):
    computers[i].add(i)

for i in range(M):
    input_ = input("").split()
    A = int(input_[0])
    B = int(input_[1])
    computers[B].add(A)

maximum = 0
numList = list(0 for i in range(N + 1))

for i in range(N + 1) :
    visit = [False for i in range(N+1)]
    cur = find(i, visit).__len__()
    numList[i] = cur
    maximum = max(cur, maximum)

for i in range(N + 1) :
    if (numList[i] == maximum) :
        print(i, end=" ")
