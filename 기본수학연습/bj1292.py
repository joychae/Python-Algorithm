# 쉽게 푸는 문제 (기본수학 연습)
# 1회차 맞은문제 80ms

import sys

start, end = map(int,sys.stdin.readline().strip().split())
numbers = []

for i in range(1, 46):
    for j in range(i):
        numbers.append(i)

print(sum(numbers[start-1:end]))