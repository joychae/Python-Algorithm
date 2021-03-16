import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().strip().split())
number_list = [i for i in range(1, N+1)]
combination = []

for i in list(combinations(number_list, M)):
    print(*list(i))