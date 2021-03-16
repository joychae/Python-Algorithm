# 스택 (스택 연습, 스택 메쏘드 구현)
# 맞은 문제
# Class 로 묶어서 풀어보자!

import sys

case = int(sys.stdin.readline().strip())

command = [list(sys.stdin.readline().strip().split()) for _ in range(case)]

stack = []

def push(num):
    global stack
    stack.append(num)

def pop():
    global stack

    if stack:
        result = stack[len(stack)-1]
        stack.pop()
        print(result)

    else:
        print(-1)

def size():
    global stack
    print(len(stack))

def empty():
    global stack
    if stack:
        print(0)
    
    else:
        print(1)

def top():
    global stack

    if stack:
        result = stack[len(stack)-1]
        print(result)
    
    else:
        print(-1)

# 만들어놓은 함수식을 command 명령어 읽어내서 대입하기
for i in range(case):
    if command[i][0] == "push":
        push(int(command[i][1]))
    
    if command[i][0] == "pop":
        pop()
    
    if command[i][0] == "size":
        size()
    
    if command[i][0] == "empty":
        empty()
    
    if command[i][0] == "top":
        top()

# print(stack)