# 분해합 (완전탐색 중 선형탐색-순차탐색 연습)
# 맞은 문제

import sys

N = int(sys.stdin.readline().strip())
M_exist = False

for i in range(1000001):
    M = i
    M_result = M + M//1000000 + (M//100000)%10 + (M//10000)%10 + (M//1000)%10 + (M//100)%10 + (M//10)%10 + M%10
    if M_result == N:
        print(M)
        M_exist = True
        break

if not M_exist:
    print("0")
    