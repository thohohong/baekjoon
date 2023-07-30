import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))

boy = list(map(int, input().split(" ")))
girl = list(map(int, input().split(" ")))

boy.sort()
girl.sort()

# N이 더 작아야함. N의 모두가 매칭되어야하는 경우
if N > M :
    N, M = M, N
    boy, girl = girl, boy

dp = [[-1 for j in range(M)] for i in range(N)]

for i in range(M) :
    dp[0][i] = abs(boy[0]-girl[i])

# dp[i][j]의 값을 구함.    
def DFS(i, j) :
    if dp[i][j] != -1 :
        return dp[i][j]
    
    minValue = 1e9
    for nextJ in range(i-1, j) :
        minValue = min(minValue, DFS(i-1, nextJ))
    
    dp[i][j] = minValue + abs(boy[i]-girl[j])
    return dp[i][j]

result = 1e9
for j in range(N-1, M) :
    result = min(result, DFS(N-1, j))

print(result)