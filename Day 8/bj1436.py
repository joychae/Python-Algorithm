# 영화감독 숌 (브루트포스-완전탐색 연습)
# 맞은 문제
# 시간복잡도 N^2

import sys

N = int(sys.stdin.readline().strip())

n =[]

for i in range(0, 7001):
    result = i * 1000 + 666
    n.append(result)

for i in range(0, 701):
    for j in range(0, 10, 1):
        result = i * 10000 + 6660 + j
        n.append(result)

for i in range (0, 71):
    for j in range(0, 100):
        result = i * 100000 + 66600 + j
        n.append(result)

for i in range (0, 8):
    for j in range(0, 1000):
        result = i * 1000000 + 666000 + j
        n.append(result)

for j in range(0, 10000):
    result = 6660000 + j
    n.append(result)

set1 = set(n)
list1 = list(set1)
list1 = sorted(list1)

print(list1[N-1])

# # 다른 풀이

# N      = int(input())  
# target = 666
# while N:
#     if '666' in str(target):
#         N -= 1
#     target += 1 
# print(target-1)