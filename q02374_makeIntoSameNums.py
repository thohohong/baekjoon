import sys
input = sys.stdin.readline

N = int(input())

sequence = []
pre = -1

for i in range(N) :
    cur = int(input())
    if cur != pre :
        sequence.append(cur)
    pre = cur

count = 0
stack = []

i = 1
stack.append(sequence[0])

while stack and i < len(sequence) :
    while stack and stack[-1] < sequence[i] :
        if len(stack) > 1 :
            if stack[-2] > sequence[i] :
                count += sequence[i] - stack[-1]
            else :
                count += stack[-2] - stack[-1]
        else :
            count += sequence[i] - stack[-1]
        stack.pop()
    stack.append(sequence[i])
    i += 1
    
if stack :
    cur = stack[-1]
    while stack :
        count += stack[-1] - cur
        cur = stack[-1]
        stack.pop()

print(count)