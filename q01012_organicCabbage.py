
T = int(input(""))
dir = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
parents = []
cabbage = []

def find(a) :
    if (a == parents[a]) :
        return a
    else :
        parents[a] = find(parents[a])
        return parents[a]

def union(a, b) :
    a = find(a)
    b = find(b)
    if (a != b) :
        if (a < b) :
            parents[b] = a
        else :
            parents[a] = b


for t in range(T):
    input_ = input("").split(" ")
    M = int(input_[0]) # width
    N = int(input_[1]) # height
    K = int(input_[2]) # number of cabbage

    parents = list(i for i in range(K))
    cabbage = list([-1 for j in range(M)] for i in range(N))

    for i in range(K) :
        input_ = input("").split(" ")
        x = int(input_[0])
        y = int(input_[1])

        cabbage[y][x] = i

        for d in dir :
            if (x + d[1] < 0 or x + d[1] >= M or y + d[0] < 0 or y + d[0] >= N):
                continue
            if (cabbage[y + d[0]][x + d[1]] != -1):
                union(cabbage[y + d[0]][x + d[1]], i)

    for i in range(K) :
        find(i)

    parents_set = set(parents)
    print(parents_set.__len__())


