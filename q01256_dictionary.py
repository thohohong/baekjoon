import sys
import math
input = sys.stdin.readline

# N : number of a
# M : number of z
# K : Kth
N, M, K = map(int, input().split(" "))

# def calculateCombination(n, c) :
#     result = 1
#     for i in reversed(range(c+1, n+1)) :
#         result *= i
#     for i in range(1, c+1) :
#         result /= i
#     return int(result)

if math.comb(N+M, N) < K :
    print(-1)
    exit(0)

count = 1
result = ""
NumA = N
NumZ = M

for idx in range(N+M) :
    if NumA == 0 :
        result += "z"
        continue
    elif NumZ == 0 :
        result += "a"
        continue

    half = math.comb(N+M-idx-1, NumA-1)
    if count + half > K :
        result += "a"
        NumA -= 1
    else :
        count += half
        result += "z"
        NumZ -= 1

print(result)