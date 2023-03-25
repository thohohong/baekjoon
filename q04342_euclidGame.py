while True :
    num1, num2 = map(int, input().split(" "))

    if (num1, num2) == (0, 0):
        exit(0)

    if num2 > num1 :
        num1, num2 = num2, num1

    def judge(turn) :
        if turn == 1 :
            print("A wins")
        elif turn == -1 :
            print("B wins")

    turn = 1
    while True :
        if num1 % num2 == 0 :
            judge(turn)
            break
        else :
            if (num1 / num2) > 2 :
                judge(turn)
                break
            else :
                num1 -= num2
                num1, num2 = num2, num1
        turn *= -1
