# 최소공배수 (정수론 및 조합론 연습)
# 맞은 문제
# BUT 유클리드 호제법으로도 다시 풀기

import sys
import math

case = int(sys.stdin.readline().strip())

for i in range(case):
    num = list(map(int,sys.stdin.readline().strip().split()))

    gcd = math.gcd(num[0], num[1])
    temp_0 = num[0]//gcd
    temp_1 = num[1]//gcd

    temp = gcd * temp_0 * temp_1

    print(temp)
