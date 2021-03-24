# 소수구하기(기본 수학)
# 1회차 틀린문제 / 2회차 맞은문제 756ms
# 에라스토테네스의 체

import sys

M, N = map(int, sys.stdin.readline().strip().split())

prime_num = [1]*1000001
prime_num[0] = 0
prime_num[1] = 0

for i in range(2, int((N**0.5))+1):
    if prime_num[i]:
        j = 2
        while i * j <= N:
            prime_num[i * j] = 0
            j += 1

for i in range(M, N+1):
    if prime_num[i]:
        print(i)