import sys
input = sys.stdin.readline

T = int(input())

for t in range(T) :
    S = input().strip()

    stat = 0
    result = 0
    for q in S :
        if q == 'O' :
            stat += 1
            result += stat
        else :
            stat = 0
    print(result)