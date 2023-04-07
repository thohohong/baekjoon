import sys
input = sys.stdin.readline

N = int(input())
field = list(map(int, input().split(" ")))

sumFromL = [0 for i in range(N)]
sumFromR = [0 for i in range(N)]

sumFromL[0] = field[0]
sumFromR[N-1] = field[N-1]

maxValue = 0
for i in range(1, N-1) :
    sumFromL[i] = sumFromL[i-1] + field[i]
    sumFromR[N-i-1] = sumFromR[N-i+1-1] + field[N-i-1]
    maxValue = max(maxValue, field[i])

if N > 2 :
    sumFromL[N-1] = sumFromL[N-2] + field[N-1]
    sumFromR[0] = sumFromR[1] + field[0]

result = 0

# target - beeA - beeB
beeB = N-1
target = 0
for beeA in range(target+1, beeB) :
    curSum = sumFromR[target] * 2 - sumFromR[beeA] - field[beeB] - field[beeA]
    result = max(result, curSum)

# beeA - target - beeB
beeA = 0
beeB = N-1
curSum = sumFromL[N-1] - field[0] - field[N-1] + maxValue
result = max(result, curSum)

# beeA - beeB - target
beeA = 0
target = N-1
for beeB in range(beeA+1, target) :
    curSum = sumFromL[target] * 2 - sumFromL[beeB] - field[beeA] - field[beeB]
    result = max(result, curSum)       


print(result)