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

def reverse(character) :
    if character == 'X' :
        return 'O'
    elif character == 'O' :
        return 'X'

def proceed(level, board, compare) :
    if level == len(O_coor) + len(X_coor) :
        if isEnd(board, 'O') or isEnd(board, 'X') :
            return True
        elif level == 9:
            return True
        else :
            return False

    if isEnd(board, 'O') or isEnd(board, 'X') :
        return False

    curCoor = X_coor
    if compare == 'O' :
        curCoor = O_coor

    for i in curCoor :
        if board[i] == '.' :
            board[i] = compare
            if proceed(level + 1, board, reverse(compare)) :
                return True
            board[i] = '.'

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
    
    board = ['.' for i in range(9)]
    result = proceed(0, board, 'X')

    if result :
        print("valid")
    else :
        print("invalid")
    board = input()