import sys
input = sys.stdin.readline

N = int(input())

stack = []
score = 0
for i in range(N) :
    curInput = input().strip()
    if curInput[0] == '1' :
        flag, A, T = map(int, curInput.split(" "))
        stack.append([A, T])
    if stack :
        stack[-1][1] -= 1
        if stack[-1][1] == 0 :
            score += stack[-1][0]
            stack.pop()

print(score)