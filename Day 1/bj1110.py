# 더하기 사이클 (while문 연습)
# 틀린 문제
# 데이터를 숫자로 가져가야 하는지, 문자열이나 리스트로 가져가야 하는지 잘 구분할 것.

i = list(map(int,input())) # [ 2, 6 ]


N = i
count = 0
while True:

    if len(i) == 1 :
        firstNumber = i[0]
        firstNumber = str(firstNumber)
    else :
        firstNumber = i[1] # [6]
        firstNumber = str(firstNumber) # "6"

    result = str(i)
    if len(result) == 1 :
        result = i[0]
        secondNumber = result[0] # "8"
    else :
        result = i[0]+i[1]
        secondNumber = result[1]

    finalNumber = firstNumber + secondNumber # "6" + "8" >> 68
    i = list(map(int,finalNumber))

    print(count)
    count += 1
    
    if N == i:
        break;

print(count)