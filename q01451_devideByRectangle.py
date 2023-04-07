import sys
input = sys.stdin.readline

board = []


# Get Input
N, M = map(int, input().split(" "))
for i in range(N) :
    board.append(list(map(int, input().strip())))

sum_dp = [[0 for j in range(M)] for i in range(N)]

def calculateSum(y, x) :
    cumulativeSum = 0
    if y != 0 :
        cumulativeSum += sum_dp[y-1][x]
    if x != 0 :
        cumulativeSum += sum_dp[y][x-1]
    if y != 0 and x != 0 :
        cumulativeSum -= sum_dp[y-1][x-1]
    cumulativeSum += board[y][x]

    sum_dp[y][x] = cumulativeSum

def calculateRangeSum(y1, x1, y2, x2) :
    sub = 0
    if y1 > 0 :
        sub += sum_dp[y1-1][x2]
    if x1 > 0 :
        sub += sum_dp[y2][x1-1]
    if y1 > 0 and x1 > 0 :
        sub -= sum_dp[y1-1][x1-1]

    return sum_dp[y2][x2] - sub

def devide() :
    result = -1
    for i in range(N-1) :
        for j in range(M-1) :
            # case 1
            num1 = sum_dp[i][j]
            num2 = sum_dp[i][M-1] - num1
            num3 = sum_dp[N-1][M-1] - sum_dp[i][M-1]

            result = max(result, num1*num2*num3)

            # case 2
            num1 = sum_dp[i][j]
            num2 = sum_dp[N-1][j] - num1
            num3 = sum_dp[N-1][M-1] - sum_dp[N-1][j]

            result = max(result, num1*num2*num3)

            # case 3
            num1 = sum_dp[i][M-1]
            num2 = sum_dp[N-1][j] - sum_dp[i][j]
            num3 = calculateRangeSum(i+1, j+1, N-1, M-1)

            result = max(result, num1*num2*num3)
    
            # case 4
            num1 = sum_dp[N-1][j]
            num2 = sum_dp[i][M-1] - sum_dp[i][j]
            num3 = calculateRangeSum(i+1, j+1, N-1, M-1)

            result = max(result, num1*num2*num3)


    # case 6
    for i in range(N-2) :
        num1 = sum_dp[i][M-1]
        for i2 in range(i+1, N-1) :
            num2 = sum_dp[i2][M-1] - num1
            num3 = sum_dp[N-1][M-1] - sum_dp[i2][M-1]

            result = max(result, num1*num2*num3)

    # case 5
    for j in range(M-2) :
        num1 = sum_dp[N-1][j]
        for j2 in range(j+1, M-1) :
            num2 = sum_dp[N-1][j2] - num1
            num3 = sum_dp[N-1][M-1] - sum_dp[N-1][j2]
            
            result = max(result, num1*num2*num3)

    return result

for i in range(N) :
    for j in range(M) :
        calculateSum(i, j)

result = devide()
print(result)