import sys

def makePattern(text, n) :
    len = 0
    
    pat = [0 for i in range(n)]
    pat[0] = 0
    
    if n == 1 :
        return pat
    idx = 1
    
    while True :
        if text[len] == text[idx] :
            pat[idx] = len + 1
            idx += 1
            len += 1
        else :
            if len != 0 :
                len = pat[len-1]
            else :
                pat[idx] = 0
                idx += 1
        if idx == n :
            break
    
    return pat

input = sys.stdin.readline

size = int(input())
text = input()

pat = makePattern(text, size)

print(size-pat[size-1])