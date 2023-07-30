import sys

input = sys.stdin.readline

X, K = map(int, input().split(" "))

X_bin = bin(X)[2:]
K_bin = bin(K)[2:]

X_idx = -1
K_idx = -1
answer = 0

while X_idx * -1 <= len(X_bin) :
    if X_bin[X_idx] == '0' :
        answer += (2 ** (X_idx * -1 - 1)) * int(K_bin[K_idx])
        X_idx -= 1
        K_idx -= 1
        if K_idx * -1 > len(K_bin) :
            break
    else :
        X_idx -= 1

while K_idx * -1 <= len(K_bin) :
    answer += (2 ** (X_idx * -1 - 1)) * int(K_bin[K_idx])
    X_idx -= 1
    K_idx -= 1

print(answer)