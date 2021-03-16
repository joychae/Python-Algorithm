# 가장 긴 증가하는 부분 수열 (동적계획법 연습)
# 틀린 문제

import sys

n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().strip().split()))

dp = [0 for i in range(n)] # n개의 0을 가진 list 생성
for i in range(n): 
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))