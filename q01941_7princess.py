import sys
from itertools import combinations, permutations
input = sys.stdin.readline

seats = []
for i in range(5) :
    seats.append(input().strip())

nums = [i for i in range(25)]
combs = list(combinations(nums, 7))

combCount = 0

DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

def adjacency(comb) :
    visit = [False for i in range(25)]
    stack = []
    stack.append(comb[0])

    count = 1
    visit[comb[0]] = True
    while stack :
        cur = stack.pop()
        r, c = cur//5, cur%5
        
        for dr, dc in DIR :
            if r+dr < 0 or r+dr >= 5 or c+dc < 0 or c+dc >= 5 :
                continue
            dem1 = (r+dr)*5 + (c+dc)
            
            if dem1 not in comb :
                continue

            if visit[dem1] :
                continue

            else :
                visit[dem1] = True
                stack.append(dem1)
                count += 1

    if count == 7 :
        return True
    else :
        return False
                
result = 0
for curComb in combs :
    sCount = 0
    for mem in curComb :
        if seats[mem//5][mem%5] == 'S' :
            sCount += 1
    if sCount < 4 :
        continue
    if adjacency(curComb) :
        result += 1

print(result)