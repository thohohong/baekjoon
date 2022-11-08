import sys
from collections import deque
import copy

def DFS(flag, include, N) :
    visit = [False for i in range(N)]
    queue = deque()

    if include.count(flag) == 0 :
        return False
    else :
        start = include.index(flag)
    
    queue.append(start)
    visit[start] = True
    
    while (not len(queue) == 0) :
        cur = queue.popleft()
        for elem in adjacent[cur] :
            if not visit[elem] and include[elem] == flag :
                visit[elem] = True
                queue.append(elem)
    
    for i in range(N) :
        if include[i] == flag and visit[i] == False :
            return False

    return True 

def makeCombination(include, i, N) :
    global min_population

    if i >= N :
        return
    
    # calculate population
    populationA = 0
    populationB = 0

    for idx in range(N) :
        if include[idx] == True :
            populationA += population[idx]
        else :
            populationB += population[idx]

    # DFS
    isValidA = DFS(True, include, N)
    isValidB = DFS(False, include, N)

    if isValidA and isValidB and abs(populationA - populationB) < min_population :
        min_population = abs(populationA - populationB)

    include_a = copy.deepcopy(include)
    include_b = copy.deepcopy(include)

    include_a[i] = True
    makeCombination(include_a, i + 1, N)

    include_b[i] = False
    makeCombination(include_b, i + 1, N)

N = int(input())

adjacent = [[] for i in range(N+1)]
population = [0] + list(map(int, input().split(" ")))

for i in range(1, N+1) :
    adjacent[i] = list(map(int, input().split(" ")))
    del adjacent[i][0]

min_population = 100000

queue = deque()
include = [False for i in range(N+1)]
include[0] = None

makeCombination(include, 1, N+1)
if min_population == 100000 :
    print(-1)
else :
    print(min_population)
