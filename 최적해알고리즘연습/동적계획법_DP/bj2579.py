# 계단오르기 (DP연습)
# 1회차 틀린문제 / 2회차 틀린문제 68ms

# 2회차 수정 코드
import sys

stair_cnt = int(sys.stdin.readline().strip())

dp = [0] * 300
stair_score = [0] * 300

for i in range(stair_cnt):
    stair_score[i] = int(sys.stdin.readline().strip())

dp[0] = stair_score[0]
dp[1] = stair_score[0] + stair_score[1]
dp[2] = max(stair_score[0] + stair_score[2], stair_score[1] + stair_score[2])

for i in range(3, stair_cnt):
    dp[i] = max(dp[i-3] + stair_score[i-1] , dp[i-2]) + stair_score[i]

print(dp[stair_cnt-1])

# # 2회차 틀린 코드
# import sys

# stair_cnt = int(sys.stdin.readline().strip())
# # 이렇게 하면 stair_cnt 가 1, 2 일때 인덱스 에러 난다.
# stair_score = [int(sys.stdin.readline()) for _ in range(stair_cnt)]

# dp = [0] * 300
# dp[0] = stair_score[0]
# dp[1] = stair_score[0] + stair_score[1]
# dp[2] = max(stair_score[0] + stair_score[2], stair_score[1] + stair_score[2])

# for i in range(3, stair_cnt):
#     dp[i] = max(dp[i-3] + stair_score[i-1] , dp[i-2]) + stair_score[i]

# print(dp[stair_cnt-1])