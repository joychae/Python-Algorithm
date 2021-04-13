# 설탕 배달 (기본수학 1 연습)
# 맞은 문제

import sys

N = int(sys.stdin.readline().strip())

bag_5 = 0

# bag 5를 최대한 쓰는 것부터 시작해, 하나씩 덜 쓰는 방향으로 경우의 수를 계산해 나간다.
for i in range(N//5, -1, -1):
    # 5와 3을 담을 수 있는 봉지만을 이용해 완벽하게 담을 수 있는지 판별해주는 조건문.
    if (N - 5*i) % 3 == 0:
        bag_5 = i
        bag_3 = (N - 5*i)//3
        bag = bag_5 + bag_3
        break
    # 안된다면 -1을 반환해주는 조건문
    else:
        bag = -1

print(bag)

# # 다른 풀이

# n     = int(input()) # 18
# count = 0 
# while True:
#     if not n % 5:
#         count += n//5
#         print(count)
#         break

#     n -= 3
#     count += 1

#     if n < 0:
#         print(-1)
#         break