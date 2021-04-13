# 회의실 배정 (그리디 알고리즘)
# 1회차 맞은문제 400ms

import sys

conference_cnt = int(sys.stdin.readline().strip())
conference_times = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(conference_cnt)]
conference_times.sort()
conference_success = [conference_times[0]]

for i in range(1, conference_cnt):
    if conference_success[-1][1] > conference_times[i][0] and conference_success[-1][1] > conference_times[i][1] :
        conference_success.pop()
        conference_success.append(conference_times[i])
    elif conference_success[-1][1] <= conference_times[i][0]:
        conference_success.append(conference_times[i])

print(len(conference_success))
    
