import sys
input = sys.stdin.readline

N = int(input())

rope = []
for i in range(N) :
    rope.append(int(input()))
rope.sort()

maxWeight = 0
for i in range(N) :
    if maxWeight <= (rope[i] * (N-i)) :
        maxWeight = rope[i] * (N-i)

print(maxWeight)