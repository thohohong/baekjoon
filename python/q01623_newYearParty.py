import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())

punkValue = [0] + list(map(int, input().split()))
super = [0, 0] + list(map(int, input().split()))
tree = dict()

# tree 구조로 만들기
for i in range(2, N+1) :
    if super[i] not in tree :
        tree[super[i]] = []
    tree[super[i]].append(i)

dp = [[-1 for i in range(N+1)] for j in range(2)]

# 탐색 순서를 위한 스택 만들기
queue = deque()
stack = deque()

queue.append(1)
stack.append(1)

while queue :
    cur = queue.popleft()
    if cur in tree :
        for next in tree[cur] :
            queue.append(next)
            stack.append(next)


queue1 = copy.deepcopy(stack)
queue2 = copy.deepcopy(stack)

# stack을 이용해 leaf부터 탐색.
while stack :
    node = stack.pop()
    result0 = 0
    result1 = punkValue[node]
    if node in tree :
        for next in tree[node] :
            result0 += max(dp[0][next], dp[1][next])
            result1 += dp[0][next]
    dp[0][node] = result0
    dp[1][node] = result1

print("%d %d"%(dp[1][1], dp[0][1]))


def trace(check, queue) :
    result = []

    while queue :
        node = queue.popleft()
        
        if check[node] :
            result.append(node)
        else :
            if node in tree :
                for next in tree[node] :
                    if dp[0][next] < dp[1][next] :
                        check[next] = True
    
    return result

check = [False for i in range(N+1)]
check[1] = True

result = trace(check, queue1)
result.sort()
for i in result :
    print(i, end=" ")
print("-1")

check = [False for i in range(N+1)]
result = trace(check, queue2)
result.sort()
for i in result :
    print(i, end=" ")
print("-1")