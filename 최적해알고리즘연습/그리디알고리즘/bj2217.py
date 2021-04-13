# 로프 (그리디 알고리즘 연습)
# 1회차 힌트 보고 푼 문제 172ms

import sys

rope_cnt = int(sys.stdin.readline().strip())
ropes = [int(sys.stdin.readline().strip()) for _ in range(rope_cnt)]
ropes.sort(reverse=True)
possible_weights = [0]*rope_cnt

for i in range(len(ropes)):
    possible_weights[i] = ropes[i]*(i+1)

print(max(possible_weights))