import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5+1)
N, M = map(int, input().split(" "))
require = [0] + list(map(int, input().split(" ")))
connect = [[] for i in range(N+1)]

for i in range(M) :
    A, B = map(int, input().split(" "))
    connect[A].append(B)
    connect[B].append(A)

check = [False for i in range(N+1)]
have = [0 for i in range(N+1)] # 각 index에서 마을이 가진 우물의 수


def DFS(node) :
    max_child_need = 0 # 자식들이 현재 node에 요청하는 우물의 수의 최대값
    sum_child_have = 0 # 자식들이 가진 우물의 수의 합

    check[node] = True

    for i in connect[node] :
        if not check[i] : # 방문한 적 없음(부모가 아님)
            max_child_need = max(max_child_need, DFS(i))
            sum_child_have += have[i]
    
    have[node] = max_child_need
    return max(0, require[node] - have[node] - sum_child_have)

tmp = DFS(1)
have[1] += tmp
print(sum(have))