# 가장 긴 증가하는 부분 수열 (동적계획법 연습 - Bottom Up)
# 1회차 틀린 문제 / 2회차 맞은 문제 148ms

import sys

num_cnt = int(sys.stdin.readline().strip())
num_list = list(map(int,sys.stdin.readline().strip().split()))
dp = [1]*num_cnt

for i in range(1, num_cnt):
    for j in range(i+1):
        if num_list[i] > num_list[j] and dp[i] <= dp[j]: # 1회차 모범 답안과 달리 나는 무조건 dp를 +1 씩 해주지 않았으므로, < 가 아니라 <=를 붙였다.
            dp[i] = dp[j] + 1

print(max(dp))

# 1회차 모범 답안

# import sys

# n = int(sys.stdin.readline().strip())
# a = list(map(int,sys.stdin.readline().strip().split()))

# dp = [0 for i in range(n)] # n개의 0을 가진 list 생성
# for i in range(n): 
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))