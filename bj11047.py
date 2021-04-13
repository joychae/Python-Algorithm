# 동전0 (그리디 알고리즘 연습)
# 맞은 문제

import sys

N, K = map(int,sys.stdin.readline().strip().split())

coins = [int(sys.stdin.readline().strip()) for i in range(N)]
coins.reverse()

count = 0
for coin in coins:
    if K//coin > 0:
        count += K//coin
        K = K - (coin * (K//coin))

    if K == 0:
        break

print(count)
