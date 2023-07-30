magic = input().strip()
devil = input().strip()
angel = input().strip()

ANGEL = 0
DEVIL = 1
bridges = [angel, devil]

dp = [[[-1 for j in range(len(magic))] for i in range(len(devil))] for k in range(2)]

def reverse(bridge) :
    if bridge == ANGEL :
        return DEVIL
    else :
        return ANGEL

def DFS(bridge, curIdx, magicIdx) :
    if magicIdx < 0 :
        return 1
    if curIdx < 0 :
        return 0
    
    if dp[bridge][curIdx][magicIdx] != -1 :
        return dp[bridge][curIdx][magicIdx]

    if bridges[bridge][curIdx] == magic[magicIdx] :
        dp[bridge][curIdx][magicIdx] = DFS(bridge, curIdx - 1, magicIdx) + DFS(reverse(bridge), curIdx-1, magicIdx-1)
    else :
        dp[bridge][curIdx][magicIdx] = DFS(bridge, curIdx-1, magicIdx)
    
    return dp[bridge][curIdx][magicIdx]

result1 = DFS(ANGEL, len(devil) - 1, len(magic) - 1)
result2 = DFS(DEVIL, len(devil) - 1, len(magic) - 1)

print(result1 + result2)