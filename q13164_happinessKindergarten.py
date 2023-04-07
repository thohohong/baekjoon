import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))
kids = list(map(int, input().split(" ")))
diff = [0 for i in range(N)]

kids.sort()
for i in range(N-1) :
    diff[i] = kids[i+1] - kids[i]

diff[N-1] = -1
diff.sort()

result = kids[N-1] - kids[0]
for i in range(1, K) :
    result -= diff[i * -1]

print(result)