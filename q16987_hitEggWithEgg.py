import sys
input = sys.stdin.readline

N = int(input())
s = []
w = []

for i in range(N) :
    S, W = map(int, input().split(" "))
    s.append(S)
    w.append(W)

def DFS(i) :
    # print(i, end=" ")
    # print(s)
    if i == N :
        return s.count(0)
    
    if s[i] <= 0 :
        return DFS(i+1)
    
    maxNum = -1
    for next in range(N) :
        if s[next] == 0 or next == i:
            continue

        pre1 = s[next]
        pre2 = s[i]

        s[next] = max(0, s[next] - w[i])
        s[i] = max(0, s[i] - w[next])

        maxNum = max(maxNum, DFS(i+1))
        
        s[next] = pre1
        s[i] = pre2
    
    if maxNum == -1 :
        return s.count(0)
    return maxNum

print(DFS(0))