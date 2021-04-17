# 지능형 기차2 (기본 수학 연습)
# 맞은 문제 68ms

import sys

peoples = [0]*10
for i in range(10):
    off, on = map(int,sys.stdin.readline().strip().split())
    if i == 0:
        peoples[i] = on
    elif i > 0:
        peoples[i]= peoples[i-1] - off + on

print(max(peoples))