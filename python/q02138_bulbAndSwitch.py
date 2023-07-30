import sys
sys.setrecursionlimit(10**5)

N = int(input())
curState = list(map(int, list(input().strip())))
targetState = list(map(int, list(input().strip())))

def reverse(num) :
    if num == 0 :
        return 1
    elif num == 1 :
        return 0

def DFS(n) :
    if n == N :
        if curState[N-1] != targetState[N-1] :
            return -1
        else :
            return 0
    result = 0

    if curState[n-1] == targetState[n-1] :
        result = DFS(n+1)
    else :
        curState[n-1] = reverse(curState[n-1])
        curState[n] = reverse(curState[n])
        if n < N-1 :
            curState[n+1] = reverse(curState[n+1])
        result = DFS(n+1)
        curState[n-1] = reverse(curState[n-1])
        curState[n] = reverse(curState[n])
        if n < N-1 :
            curState[n+1] = reverse(curState[n+1])

        if result != -1 :
            result += 1

    return result

result1 = DFS(1)
curState[0] = reverse(curState[0])
curState[1] = reverse(curState[1])
result2 = DFS(1)

if result1 == -1 and result2 == -1 :
    print(-1)
elif result1 != -1 and result2 != -1 :
    print(min(result1, result2+1))
elif result1 == -1 :
    print(result2 + 1)
else :
    print(result1)