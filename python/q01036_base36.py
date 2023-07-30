import sys
from collections import deque

input = sys.stdin.readline

def base36(num) :
    if num >= 0 and num <= 9 :
        return chr(num + ord('0'))
    else :
        return chr(num - 10 + ord('A'))

def base10to36(num) :
    result = deque()
    while num > 0 :
        result.appendleft(base36(int(num % 36)))
        num = num//36
    return result

N = int(input())
num = []
count = [0 for i in range(36)]

# Get input and calculate count
orgSum = 0
for i in range(N) :
    cur = input().strip()
    orgSum += int(cur, 36)
    for j in range(len(cur)) :
        count[int(cur[j], 36)] += pow(36, len(cur)-j-1)


# calculate orginSum(orgSum) and construct numList
for i in range(36) :
    count[i] = (35 - i) * count[i]

K = int(input())
count.sort(reverse=True)

result = orgSum
for i in range(K) :
    result += count[i]

if result == 0 :
    print(result)
else :
    result = ''.join(base10to36(result))
    print(result)