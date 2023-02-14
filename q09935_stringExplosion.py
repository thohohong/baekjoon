import sys
input = sys.stdin.readline

org = input().strip()
exp = input().strip()

s = [] # stack, (char, sameIdx)

for i in range(len(org)) :
  if not s : # empty
    if exp[0] == org[i] :
      if len(exp) == 1 :
        continue
      s.append((org[i], 0))
    else :
      s.append((org[i], -1))
  else :
    idx = s[-1][1] + 1
    if org[i] == exp[idx] :
      if idx == len(exp) - 1 : # explosion string
        for j in range(len(exp) - 1) :
          s.pop()
      else :
        s.append((org[i], idx))
    else :
      if org[i] == exp[0] :
        s.append((org[i], 0))
      else :
        s.append((org[i], -1))

if s :
  for i in s :
    print(i[0], end="")
else :
  print("FRULA")