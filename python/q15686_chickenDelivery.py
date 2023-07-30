import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
field = []

house = []
chicken = []

# (distance, chicken num)쌍으로 이루어진 리스트들에서 삭제되지 않은 가장 앞에 있는 쌍을 return
def findPossible(chickenDistanceList) :
    for i in range(len(chickenDistanceList)) :
        if not checkDel[chickenDistanceList[i][1]] :
            return chickenDistanceList[i]

minIncreasing = 1e9

# idx : searchOrder's idx.
# increasing : 원래 값에서 증가한 chicken distance
# * checkdel : global variable. 삭제된 치킨집을 관리
def DFS(idx, increasing) :
    global minIncreasing
    if increasing > minIncreasing :
        return
    if idx == len(searchOrder) :
        if checkDel.count(False) <= M :
            minIncreasing = increasing
        return
    
    curChicken = searchOrder[idx]
    
    # 현재 idx의 치킨집을 삭제하지 않음
    DFS(idx+1, increasing)

    # 현재 idx의 치킨집을 삭제함
    # 추가 증가값 계산
    if checkDel.count(True) == len(chicken) - 1 :
        return
    
    curIncreasing = 0
    for i in range(len(house)) :
        pre = findPossible(chickenDistances[i])
        checkDel[curChicken] = True
        cur = findPossible(chickenDistances[i])
        checkDel[curChicken] = False

        if pre[1] != cur[1] :
            curIncreasing += cur[0] - pre[0] # distance diff
    
    checkDel[curChicken] = True
    DFS(idx+1, increasing + curIncreasing)
    checkDel[curChicken] = False


for i in range(N) :
    field.append(list(map(int, input().split(" "))))
    for j in range(N) :
        if field[i][j] == 1 :
            house.append((i, j))
        elif field[i][j] == 2 :
            chicken.append((i, j))


table = [[0 for j in range(len(house))] for i in range(len(chicken))]
chickenDistances = [[] for i in range(len(house))]

for i in range(len(house)) :
    for j in range(len(chicken)) :
        distance = abs(chicken[j][0] - house[i][0]) + abs(chicken[j][1] - house[i][1])
        chickenDistances[i].append((distance, j))
        table[j][i] = distance
    chickenDistances[i].sort()

# chicken restaurant's order to search - in decreasing order of sum of chicken distance per house
searchOrder = [i for i in range(len(chicken))]
searchOrder.sort(key=lambda x : sum(table[x]) * -1)

checkDel = [False for i in range(len(chicken))]
DFS(0, 0)

result = minIncreasing
# calculate increasing
for i in range(len(house)) :
    result += chickenDistances[i][0][0]

print(result)