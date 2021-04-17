# 이진수 (기본 수학 연습)
# 1회차 틀린문제

import sys

case = int(sys.stdin.readline().strip())

for _ in range(case):
    num = int(sys.stdin.readline().strip())
    i = 0
    while num > 0:
        if num % 2 == 1:
            print(i, end = ' ')
        num = num//2
        i += 1