# N 번째 큰 수 (정렬 연습)
# 1회차 92ms
# 1회차는 선택정렬로 구현해보았습니다

import sys

case = int(sys.stdin.readline().strip())
for _ in range(case):
    numbers = list(map(int,sys.stdin.readline().strip().split()))

    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                numbers[min_idx], numbers[j] = numbers[j], numbers[min_idx]

    print(numbers[7])