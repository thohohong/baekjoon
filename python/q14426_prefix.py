import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))

head = dict()

for i in range(N) :
    sen = input().strip()
    node = head
    
    for ch in sen :
        if ch not in node :
            node[ch] = dict()
        node = node[ch]

fail = 0
for i in range(M) :
    sen = input().strip()

    node = head
    for ch in sen :
        if ch not in node :
            fail += 1
            break
        node = node[ch]

print(M - fail)