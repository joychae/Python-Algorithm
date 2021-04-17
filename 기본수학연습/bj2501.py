# 약수 구하기 (기본 수학 연습)
# 1회차 맞은문제 84ms

import sys

N, K = map(int, sys.stdin.readline().strip().split())
numbers = [i+1 for i in range(N)]
divisors = []

for i in numbers:
    if N % i == 0:
        divisors.append(i)

if len(divisors) >= K:
    print(divisors[K-1])
elif len(divisors) < K:
    print(0)