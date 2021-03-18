# 블랙잭 (완전탐색 연습)
# 맞은 문제 (BUT DFS로 조합, 순열 구하는거 공부해두자)

import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().strip().split())
number_list = list(map(int,sys.stdin.readline().strip().split()))
combination_sum = []

for i in list(combinations(number_list, 3)):
    if sum(i) <= M:
        combination_sum.append(sum(i))

print(max(combination_sum))
         
