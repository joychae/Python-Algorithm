# 주유소 (그리디 알고리즘 연습)

import sys

city_cnt = int(sys.stdin.readline().strip())
city_distances = list(map(int,sys.stdin.readline().strip().split()))
city_oil_prices = list(map(int,sys.stdin.readline().strip().split()))

for i in range(city_cnt-1):

# # 시간 초과 풀이

# import sys

# city_cnt = int(sys.stdin.readline().strip())
# city_distances = list(map(int,sys.stdin.readline().strip().split()))
# city_oil_prices = list(map(int,sys.stdin.readline().strip().split()))
# cheapest_oil_price = min(city_oil_prices[:-1])
# total_oil_price = 0
# total_oil_price += cheapest_oil_price * sum(city_distances[city_oil_prices.index(cheapest_oil_price):])

# while True:

#     if city_oil_prices.index(cheapest_oil_price) == 0:
#         break

#     former_cheapest_oil_price = cheapest_oil_price
#     temp_cheapest_oil_price = min(city_oil_prices[:city_oil_prices.index(cheapest_oil_price)])
#     cheapest_oil_price = temp_cheapest_oil_price
#     total_oil_price += cheapest_oil_price * sum(city_distances[city_oil_prices.index(cheapest_oil_price):city_oil_prices.index(former_cheapest_oil_price)])    

# print(total_oil_price)