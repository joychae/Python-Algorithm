# 최대공약수와 최소공배수 (정수론 및 조합론)
# 맞은 문제
# 유클리드 호제로도 풀어보기!

import sys
import math

num = list(map(int,sys.stdin.readline().strip().split()))

gcd = math.gcd(num[0],num[1])

temp_0 = num[0]//gcd
temp_1 = num[1]//gcd

lcm = gcd * temp_0 * temp_1

list = [gcd, lcm]

for n in list:
    print(n)
