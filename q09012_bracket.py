testCaseNum = int(input())

for testCase in range(testCaseNum) :
    str = input().strip()
    s = []
    isSuccess = True

    for c in str :
        if c == '(' :
            s.append('(')
        else :
            if not s :
                isSuccess = False
                break
            else :
                s.pop()
    
    if isSuccess and not s:
        print("YES")
    else :
        print("NO")