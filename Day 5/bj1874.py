# 스택 수열 (스택 연습)
# 틀린 문제

import sys

num = int(sys.stdin.readline().strip())

count = 0
stack = []
result = []
no_message = True


while True:
    for i in range(num):
        x = int(sys.stdin.readline().strip())

        while count < x :
            count += 1
            stack.append(count)
            result.append("+")
        
        if stack[-1] == x:
            stack.pop()
            result.append("-")

        else:
            no_message = False
            exit(0)

if no_message ==  False:
    print("NO")
else:
    print(result)