import sys
from collections import deque

T = int(input())

for _ in range(T) :
    N = int(input())
    line = deque(input().strip())

    # 각 그룹의 마지막 위치 갱신
    coor = dict()
    memberCount = dict()

    for i in range(N) :
        coor[line[i]] = i
        if line[i] in memberCount :
            memberCount[line[i]] += 1
        else :
            memberCount[line[i]] = 1
    
    lastCoor = []
    for elem in coor :
        lastCoor.append((coor[elem], elem))

    lastCoor = deque(sorted(lastCoor))
    
    idx = 0
    result = 0

    isOut = [False for i in range(N)]

    while lastCoor :
        curTeamLastIdx, curTeam = lastCoor.popleft()
        
        yieldCount = 0
        nextIdx = -1

        for i in range(idx, curTeamLastIdx+1) :
            if line[i] == curTeam :
                isOut[i] = True
            else :
                if not isOut[i] :
                    yieldCount += 1
                    if nextIdx == -1 :
                        nextIdx = i
        
        result += yieldCount * memberCount[curTeam]

        if nextIdx == -1 :
            idx = curTeamLastIdx + 1
        else :
            idx = nextIdx
    
    print(result * 5)