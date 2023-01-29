import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(" "))

knowTruth = list(map(int, input().split(" ")))
del knowTruth[0]

partyGraph = [set() for i in range(M)] # 파티끼리의 연결성.
partyCanLie = [True for i in range(M)] # 파티에서 거짓말을 할 수 있는지의 여부

guestGoParty = [[] for i in range(N + 1)] # 각 게스트가 참여한 파티

for curParty in range(M) :
  # Get Input
  guestList = list(map(int, input().split(" ")))
  del guestList[0]

  for curGuest in guestList :
    if curGuest in knowTruth :
      partyCanLie[curParty] = False

    # 현재 node를 갱신
    partyGraph[curParty].update(guestGoParty[curGuest])
    guestGoParty[curGuest].append(curParty)

    # 상대 node를 갱신
    for preParty in guestGoParty[curGuest] :
      partyGraph[preParty].add(curParty)

check = [False for i in range(M)]

def DFS(node) :
  if check[node] :
    return
  check[node] = True

  partyCanLie[node] = False
  for i in partyGraph[node] :
    DFS(i)

for i in range(M) :
  if partyCanLie[i] == False :
    DFS(i)

sum = 0
for i in range(M):
  if partyCanLie[i] == True :
    sum += 1

print(sum)