# ATM (그리디 알고리즘 연습)
# 맞은 문제
# DP Bottom Up 방식 적용!

import sys

people = int(sys.stdin.readline().strip())

time = list(map(int, sys.stdin.readline().strip().split()))
time.sort()

time_spent =[]

for i in range(len(time)):
    if i == 0:
        result = time[0]
        time_spent.append(result)
    
    else:
        result = time_spent[i-1] + time[i]
        time_spent.append(result)

print(sum(time_spent))