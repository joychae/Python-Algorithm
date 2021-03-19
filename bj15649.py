import itertools
import sys

N, M = map(int,sys.stdin.readline().strip().split())
num_list = [i for i in range(1,N+1)]

for i in list(itertools.permutations(num_list,M)):
    print(*list(i))