# 우주 가기 문제 (기본 수학 연습)
# 틀린 문제

import sys

case = int(sys.stdin.readline().strip())

def space(x, y):

    distance = y - x

    sum_num = 0
    count = 0
    for i in range(1, distance//2 +1):
        sum_num += i
        if sum_num <= distance//2:
            count += 1
            break

    count = count*2
    remain = distance - sum_num*2

    for j in range(i+1, 0, -1):
        if remain//j >= 1:
            remain -= j
            count += 1
        if remain == 0:
            break

    return count

ans = []
for _ in range(case):
    x, y = map(int,sys.stdin.readline().strip().split())
    ans.append(space(x, y))

for i in ans:
    print(i)

