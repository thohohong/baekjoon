import math

N = int(input())

charToNum = dict()

for i in range(N) :
    word = input()
    decimal = math.pow(10, len(word) - 1)   
    for j in word :
        value = charToNum.get(j, 0)
        charToNum[j] = value + decimal
        decimal /= 10

sortedValue = sorted(charToNum.values(), reverse=True)

sum = 0
curNum = 9
for elem in sortedValue :
    sum += curNum * elem
    curNum -= 1

print(int(sum))