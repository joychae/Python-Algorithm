# 약수 (정수론 및 조합론)
# 틀린 문제 (접근법 구글링함)

import sys

N = int(sys.stdin.readline().strip())

num = list(map(int,sys.stdin.readline().strip().split()))
num.sort()

print(num[0]*num[-1])