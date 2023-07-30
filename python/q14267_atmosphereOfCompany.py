import sys

input = sys.stdin.readline
sys.setrecursionlimit(100010)
def doCompliment(person, amount) :
  compliment[person] += amount

  if person in subordinate :
    for sub in subordinate[person] :
      doCompliment(sub, compliment[person])

N, M = map(int, input().split(' '))

superior = list(map(int, input().split(' ')))
subordinate = dict()
compliment = [0 for i in range(N)]

for i in range(N) :
  if superior[i]-1 not in subordinate :
    subordinate[superior[i]-1] = []
  subordinate[superior[i]-1].append(i)

for i in range(M) :
  person, amount = map(int, input().split(" "))
  compliment[person - 1] += amount

doCompliment(0, 0)
for i in compliment :
  print(i, end=" ")