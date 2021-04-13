# 거스름돈 (그리디 알고리즘 연습)

import sys

product_price = int(sys.stdin.readline().strip())
change_price = 1000 - product_price
coins = [500, 100, 50, 10, 5, 1]
coin_cnt = 0

for coin in coins:
    temp_change_price = change_price%coin
    coin_cnt += change_price//coin
    change_price = temp_change_price
    if change_price == 0:
        print(coin_cnt)
        break