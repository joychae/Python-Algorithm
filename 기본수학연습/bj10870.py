# 피보나치 수 5 (기본 수학 연습)
# 1회차 맞은 문제 68ms

import sys

dp = [0]*21
dp[0] = 0
dp[1] = 1

for i in range(2, 21):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[int(sys.stdin.readline().strip())])