# 분해합 (완전탐색 중 선형탐색-순차탐색 연습)
# 1회차 맞은 문제 712ms / 2회차 맞은 문제 680ms

import sys

target = int(sys.stdin.readline().strip())
constructor_exist = 0

for i in range(target+1):
    digit_sum = i + (i//1000000)%10 +(i//100000)%10 + (i//10000)%10 + (i//1000)%10 + (i//100)%10 + (i//10)%10 + i%10
    if digit_sum == target:
        constructor_exist = 1
        print(i)
        break

if not constructor_exist:
    print(0)
    