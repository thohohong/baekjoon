import sys
input = sys.stdin.readline

origin = input().strip()
change = input().strip()

i, j = 0, 0
while i < len(origin) and i < len(change) and origin[i] == change[i] :
  i += 1
while j < len(origin) and j < len(change) and origin[len(origin)-j-1] == change[len(change)-j-1] :
  j += 1

j = len(change) - j

# if i > j and len(change) > len(origin) :
#   print(len(change) - len(origin))
# elif i > j and len(change) < len(origin) :
#   print(0)
# else :
#   print(j-i)
print(max(len(change)-len(origin), j - i, 0))