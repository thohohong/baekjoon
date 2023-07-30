import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
head = dict()

for i in range(N) :
    cur = deque(input().strip().split(" "))
    cur.popleft()

    curNode = head
    for elem in cur :
        if elem in curNode :
            curNode = curNode[elem]
        else :
            curNode[elem] = dict()
            curNode = curNode[elem]

def treversal(node, level) :
    for nextNode in sorted(node) :
        for i in range(level) :
            print("--", end="")
        print(nextNode)
        treversal(node[nextNode], level+1)

treversal(head, 0)