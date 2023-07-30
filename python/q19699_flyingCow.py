import sys



def check_is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

N, M = map(int, input().split())
weights = list(map(int, input().split()))

answer = set()

def DFS(idx, sum, count) :
    if count == M :
        if check_is_prime(sum) :
            answer.add(sum)
        return
    
    if idx >= N :
        return
    
    # include
    DFS(idx + 1, sum + weights[idx], count + 1)

    # not include
    DFS(idx + 1, sum, count)

DFS(0, 0, 0)

answer = sorted(list(answer))

if answer :
    for i in range(len(answer)) :
        print(answer[i], end="")
        if i != len(answer)-1 :
            print(" ", end="")
    print()
else :
    print(-1)