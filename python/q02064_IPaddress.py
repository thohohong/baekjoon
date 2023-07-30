import sys
input = sys.stdin.readline

N = int(input())

def IPtoNum(IP) :
    nums = list(map(int, IP.split(".")))
    result = 0
    for i in range(4) :
        result = result << 8
        result += nums[i]
    return result

def numToIP(num) :
    nums = [0, 0, 0, 0]

    for i in reversed(range(4)) :
        nums[i] = num & 0b11111111
        num = num >> 8

    
    return ".".join(list(map(str, nums)))

def XOR(num1, num2) :
    if num1 == num2 :
        return 1
    else :
        return 0

min_IP = 1 << 32
max_IP = 0

for _ in range(N) :
    cur = IPtoNum(input().strip())
    
    min_IP = min(min_IP, cur)
    max_IP = max(max_IP, cur)

compare = 0b10000000000000000000000000000000
mask = 0

isFound = False
for i in range(32) :
    if not isFound :
        if XOR(min_IP & compare, max_IP & compare) == 1 :
            mask += 1
            compare = compare >> 1
        else :
            mask += 1
            isFound = True
    mask = mask << 1
if not isFound :
    mask += 1

print(numToIP(max_IP & mask))
print(numToIP(mask))