import sys
input = sys.stdin.readline

scales = list(map(int, input().split(" ")))

diff = scales[1] - scales[0]
for i in range(2, 8) :
    if scales[i] - scales[i-1] != diff :
        print("mixed")
        exit(0)

if diff == -1 :
    print("descending")
else :
    print("ascending")