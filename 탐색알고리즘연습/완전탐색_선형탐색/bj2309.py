# 일곱 난쟁이 (브루트포스 연습)
# 1회차 맞은문제 72ms

import sys
from itertools import combinations

heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
idx = [i for i in range(9)]
idx_combinations = list(combinations(idx, 2))

for i in range(len(idx_combinations)):
    temp_heights = heights.copy()
    x, y = idx_combinations[i]
    temp_heights[x] = 0
    temp_heights[y] = 0
    sum_heights = sum(temp_heights)

    if sum_heights == 100:
        break

temp_heights.sort()
for i in temp_heights[2:]:
    print(i)
