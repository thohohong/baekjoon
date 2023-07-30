import sys
import math
input = sys.stdin.readline

word = dict()
word["ZE"] = (0, 4)
word["ON"] = (1, 3)
word["TW"] = (2, 3)
word["TH"] = (3, 5)
word["FO"] = (4, 4)
word["FI"] = (5, 4)
word["SI"] = (6, 3)
word["SE"] = (7, 5)
word["EI"] = (8, 5)
word["NI"] = (9, 4)

numToWord = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def printNumToWord(num) :
  if abs(math.floor(num)) > abs(math.ceil(num)) :
    num = math.ceil(num)
  else :
    num = math.floor(num)

  for i in str(int(num)) :
    if i == '-' :
      print(i, end="")
    else :
      print(numToWord[int(i)], end="")
  print("")
  
def processExp(exp, curNum) :
  global convertedStr
  convertedStr += str(curNum)
  convertedStr += exp
  numStack.append(curNum)
  calculate(exp)

def calculate(curExp) :
  if expStack :
    num1 = numStack.pop()
    num2 = numStack.pop()
    exp = expStack.pop()
    if exp == '+' :
      numStack.append(num2 + num1)
    if exp == '-' :
      numStack.append(num2 - num1)
    if exp == 'x' :
      numStack.append(num2 * num1)
    if exp == '/' :
      if abs(math.floor(num2 / num1)) > abs(math.ceil(num2 / num1)) :
        numStack.append(math.ceil(num2 / num1))
      else :
        numStack.append(math.floor(num2 / num1))
  expStack.append(curExp)

origin = input().strip()
convertedStr = ""
curNum = 0
resultNum = 0

expStack = []
numStack = []

i = 0
if origin[len(origin) - 1] != '=' :
  print("Madness!")
  exit(0)

while i < len(origin) :
  if origin[i] == '+' or origin[i] == '-' or origin[i] == 'x' or origin[i] == '/' or origin[i] == '=':
    if curNum == 0:
      print("Madness!")
      exit(0)
    processExp(origin[i], curNum)
    curNum = 0
    i += 1
  else :
    try :
      info = word[origin[i:i+2]]
    except :
      print("Madness!")
      exit(0)
    if i+info[1] >= len(origin) or origin[i:i+info[1]] != numToWord[info[0]] :
      print("Madness!")
      exit(0)
    curNum *= 10
    curNum += info[0]
    i += info[1]

print(convertedStr)
printNumToWord(numStack[0])