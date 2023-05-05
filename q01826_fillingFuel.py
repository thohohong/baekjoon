import sys
input = sys.stdin.readline

N = int(input())
station = [] # (b, a) : b is fuel, a is position
visit = [False for i in range(N)]

for i in range(N):
    a, b = map(int, input().split(" "))
    station.append((b, a))

L, P = map(int, input().split(" "))
station = sorted(station, reverse=True)

count = 0

while L > P :
    idx = 0
    while station[idx][1] > P or visit[idx] :
        idx += 1
        if idx >= N :
            print(-1)
            exit(0)
    P += station[idx][0]
    visit[idx] = True
    count += 1

print(count)