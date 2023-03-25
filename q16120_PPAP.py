inputStr = input().strip()

stack = []
compare = ['A', 'P', 'P']

flag = True

for i in range(len(inputStr)) :
    flag = False
    if inputStr[i] == 'P' :
        if len(stack) >= 3 :
            flag = True
            for j in range(3) :
                if stack[(j+1) * -1] != compare[j] :
                    flag = False

    if flag :
        stack.pop()
        stack.pop()
    else :
        stack.append(inputStr[i])

if len(stack) != 1 or stack[0] != 'P' :
    print("NP")
else :
    print("PPAP")

