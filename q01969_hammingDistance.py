userInput = input("").split(" ")

DNA_num = int(userInput[0])
length = int(userInput[1])

DNA_info = [[0 for i in range(4)] for i in range(length)]

charToInt = {'A': 0, 'C' : 1, 'G' : 2, 'T' : 3}
intToChar = {0 : 'A', 1 : 'C', 2: 'G', 3 : 'T'}

for i in range(DNA_num) :
    userInput = input("")
    for j in range(length) :
        curChar = charToInt.get(userInput[j])
        DNA_info[j][curChar] += 1

hammingDistance = 0

for i in range(length) :
    max = 0
    maxIdx = 0
    for j in range(4) :
        if DNA_info[i][j] > max : 
            max = DNA_info[i][j]
            maxIdx = j
    print(intToChar.get(maxIdx), end="")
    hammingDistance += DNA_num - max

print("")
print(hammingDistance)