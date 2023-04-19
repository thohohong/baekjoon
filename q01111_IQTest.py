import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split(" ")))


if N < 2 :
    print("A")
    exit(0)

# calculate
if seq[0] == seq[1] :
    a = 1
    b = 0
elif N < 3 :
    print("A")
    exit(0)
else :
    a = (seq[1]-seq[2]) / (seq[0]-seq[1])
    b = seq[1] - seq[0] * a

if a % 1 != 0 or b % 1 != 0 :
    print("B")
    exit(0)
    
# test
for i in range(N-1) :
    num1 = seq[i]
    num2 = seq[i+1]
    if num2 != a * num1 + b :
        print("B")
        exit(0)

result = int(seq[N-1] * a + b)
print(result)