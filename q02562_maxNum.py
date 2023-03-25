maxNum = 0
maxIdx = 0

for i in range(9):
    cur = int(input())
    if cur > maxNum :
        maxNum = cur
        maxIdx = i

print(maxNum)
print(maxIdx+1)