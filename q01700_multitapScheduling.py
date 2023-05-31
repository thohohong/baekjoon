from collections import deque

plugNum, useNum = map(int, input().split(" "))
order = list(map(int, input().split(" ")))

time = [deque() for i in range(useNum+1)]

for i in range(useNum) :
    time[order[i]].append(i)

tab = [0 for i in range(plugNum)]

result = 0
for idx in range(useNum) :
    if order[idx] in tab :
        # time[order[idx]].popleft()
        continue
    if 0 in tab :
        for t in range(plugNum) :
            if tab[t] == 0 :
                tab[t] = order[idx]
                break
                # time[order[idx]].popleft()
        continue
    
    changeTab = 0
    maxTime = -1

    for t in range(plugNum) :
        while time[tab[t]] and time[tab[t]][0] < idx :
            time[tab[t]].popleft()
        
        if not time[tab[t]] :
            changeTab = t
            break
        
        if time[tab[t]][0] > maxTime :
            maxTime = time[tab[t]][0]
            changeTab = t

    tab[changeTab] = order[idx]
    # time[order[idx]].popleft()
    result += 1

print(result)