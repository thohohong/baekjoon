N = int(input())
sequence = list(map(int, input().split(" ")))

MAX = max(sequence)
MIN = min(sequence)

print("%d %d"%(MIN, MAX))