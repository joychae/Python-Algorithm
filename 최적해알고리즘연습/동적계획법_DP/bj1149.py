# RGB거리 (DP 연습문제)
# 1회차 틀린 문제 / 2회차 맞은 문제 64ms
# 1회차 - Bottom up DP 방식 많이 연습해야 한다!

import sys

house_cnt = int(sys.stdin.readline())
cost_per_home = []

for _ in range(house_cnt):
    cost_per_home.append(list(map(int,sys.stdin.readline().split())))

dp = [cost_per_home[0]]

for i in range(1, house_cnt):
    cost_per_color = []

    temp_red = min(dp[i-1][1], dp[i-1][2])
    cost_per_color.append(temp_red + cost_per_home[i][0])

    temp_green = min(dp[i-1][0], dp[i-1][2])
    cost_per_color.append(temp_green + cost_per_home[i][1])

    temp_blue = min(dp[i-1][0], dp[i-1][1])
    cost_per_color.append(temp_blue + cost_per_home[i][2])

    dp.append(cost_per_color)

print(min(dp[-1]))