# 빗물 (시뮬레이션 연습/ 브루트포스)
# 1회차 맞은문제 68ms

import sys

H, W = map(int,sys.stdin.readline().strip().split())
buildings = list(map(int,sys.stdin.readline().strip().split()))
raindrops = 0

for i in range(1, len(buildings)-1):
    left_max = max(buildings[:i])
    right_max = max(buildings[i+1:])

    raindrop = min(left_max, right_max) - buildings[i]
    if raindrop > 0:
        raindrops += raindrop

print(raindrops)