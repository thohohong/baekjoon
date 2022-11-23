import sys

def findDepth(a) :
    multiplier = 1
    while True :
        if a >= multiplier :
            multiplier *= 2
        else :
            return multiplier


input = sys.stdin.readline

testCase = int(input())

for i in range(testCase) :
    a, b = map(int, input().split(" "))
    if b < a :
        a, b = b, a
    
    depthLimit = findDepth(a)
    while b >= depthLimit :
        b = int(b/2)
    while a != b :
        a = int(a/2)
        b = int(b/2)

    print(a * 10)