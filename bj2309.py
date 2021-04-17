# 일곱 난쟁이 (브루트포스 연습)

import sys
from itertools import combinations

heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
idx = [i for i in range(9)]
idx_combinations = list(combinations(idx, 2))

for i in range(len(idx_combinations)):
    temp_heights = heights.copy()
    print(temp_heights)
    x, y = idx_combinations[i]
    print(x)
    print(y)
    del temp_heights[x]
    del temp_heights[y]
    sum_heights = sum(temp_heights)

    if sum_heights == 100:
        print(temp_heights)
        break

