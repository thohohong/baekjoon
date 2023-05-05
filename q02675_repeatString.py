import sys
input = sys.stdin.readline

T = int(input())

for t in range(T) :
    R, S = input().split(" ")
    R = int(R)
    S = S.strip()

    for char in S :
        for i in range(R) :
            print(char, end="")
    print("")