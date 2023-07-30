N, M = map(int, input().split())

pos = list(map(int, input().split()))
pos.sort()

result = 0
firstStep = -1
# minus
i = 0
while i < N and pos[i] < 0 :
    firstStep = max(firstStep, pos[i] * -1)
    result += (pos[i] * -1) * 2
    i += M

# plus
i = N-1
while i >= 0 and pos[i] > 0 :
    firstStep = max(firstStep, pos[i])
    result += pos[i] * 2
    i -= M

print(result - firstStep)