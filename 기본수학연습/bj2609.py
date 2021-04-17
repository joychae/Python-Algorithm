# 최대공약수와 최소공배수 (정수론 및 조합론)
# 1회차 맞은 문제 68ms / 2회차 틀린 문제
# 유클리드 호제로도 풀어보기!
# 2회차 - 유클리드 호제법 공식 외워드기

import sys

A, B = map(int,sys.stdin.readline().strip().split())
a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

print(a)
print((A * B)//a)

# 1회차 파이썬 내장함수로 푼 문제

# import sys
# import math

# num = list(map(int,sys.stdin.readline().strip().split()))

# gcd = math.gcd(num[0],num[1])

# temp_0 = num[0]//gcd
# temp_1 = num[1]//gcd

# lcm = gcd * temp_0 * temp_1

# list = [gcd, lcm]

# for n in list:
#     print(n)