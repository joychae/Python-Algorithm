# 스택 수열 (스택 연습)
# 1회차 틀린 문제 / 2회차 맞은 문제 252ms
# 1회차 때 시간 상 건드리지도 않고 넘어간 문제라 2회차 풀이임에도 좀 지저분하다.

import sys

num_cnt = int(sys.stdin.readline().strip())
num_target = [int(sys.stdin.readline().strip()) for _ in range(num_cnt)]
num_target.reverse() #pop(0)이 아닌 pop()을 사용해 시간 복잡도를 줄이기 위함
cnt = 0
stack = []
plus_minus_stack = []

while num_target:
    
    if not stack: # 아래의 if, elif 조건문이 num_target, stack 인덱스를 부르고 있어서 인덱스에러 방지 차원에서 stack이 빌 경우를 따로 설정
        cnt += 1
        stack.append(cnt)
        plus_minus_stack.append("+")

    if num_target[-1] == stack[-1]:
        num_target.pop()
        stack.pop()
        plus_minus_stack.append("-")

    elif num_target[-1] != stack[-1]:
        cnt += 1
        stack.append(cnt)
        plus_minus_stack.append("+")
    
    if cnt > num_cnt:
        print("NO")
        break

if not num_target:
    for plus_minus in plus_minus_stack:
        print(plus_minus)