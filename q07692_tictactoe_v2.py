import sys

def isEnd(board, compare) :
    boardBinary = 0
    for i in range(9) :
        boardBinary = boardBinary << 1
        if board[i] == compare :
            boardBinary += 1
    
    for i in case :
        if boardBinary & i == i :
            return True
    
    return False

input = sys.stdin.readline

case = [0b111000000,
        0b000111000,
        0b000000111,
        0b100010001,
        0b001010100,
        0b100100100,
        0b010010010,
        0b001001001]

board = input()
while board != "end\n" :
    O_coor = []
    X_coor = []
    for i in range(9) :
        if board[i] == 'X' :
            X_coor.append(i)
        elif board[i] == 'O' :
            O_coor.append(i)

    result = False
    board = list(board)

    if len(X_coor) < len(O_coor) :
        result = False
    elif len(X_coor) - len(O_coor) > 1 :
        result = False
    elif len(X_coor) == len(O_coor) and isEnd(board, 'X') :
        result = False
    elif isEnd(board, 'X') and isEnd(board, 'O') :
        result = False
    elif len(X_coor) - len(O_coor) == 1 and isEnd(board, 'O') :
        result = False
    elif len(X_coor) + len(O_coor) < 9 :
        if not isEnd(board, 'X') and not isEnd(board,'O') :
            result = False
        else :
            result = True
    else :
        result = True
    
    if result :
        print("valid")
    else :
        print("invalid")
    board = input()