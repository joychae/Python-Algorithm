# 최소, 최대 (기본 수학 문제)
# 맞은 문제 588ms
# max, min 과 같은 내장함수 안 쓰고 직접 구현해보았다.
# max, min 을 사용한 다른 답안과 시간이 비슷하게 걸린 것을 보아 max, min 도 비슷한 로직인 듯 하다.

import sys

case = int(sys.stdin.readline().strip())
numbers = list(map(int,sys.stdin.readline().strip().split()))
max_num = numbers[0]
min_num = numbers[0]

for i in range(1, case):
    if numbers[i] > max_num:
        max_num = numbers[i]
    if numbers[i] < min_num:
        min_num = numbers[i]

print(min_num, max_num)