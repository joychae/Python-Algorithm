# 멀티탭 스케줄링 (그리디 알고리즘 연습)

import sys

hole_cnt, use_cnt = map(int,sys.stdin.readline().strip().split())
use_order = list(map(int,sys.stdin.readline().strip().split()))
use_now = [0]*hole_cnt
off_cnt = 0

for use in use_order:
    if use in use_now:
        continue
    if 
    # elif use not in use_now:
    #     off_cnt += 1
    #     for i in use_now:
    #         if i not in use_order[use_order.index(use):]:
    #             use_now[use_now.index(i)] = use
    #             break 
    #         else:
