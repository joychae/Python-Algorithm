# 종이의 개수
# 1회차 맞은 문제 6028ms

import sys

side = int(sys.stdin.readline().strip())
paper_data_list = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(side)]
plus_data_cnt = 0
zero_data_cnt = 0
minus_data_cnt = 0

def divide(x, y, n):
    global plus_data_cnt, zero_data_cnt, minus_data_cnt
    paper_data_type = paper_data_list[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper_data_type != paper_data_list[i][j]:
                divide(x, y, n//3)
                divide(x, y+n//3, n//3)
                divide(x, y+2*(n//3), n//3)
                divide(x+n//3, y, n//3)
                divide(x+n//3, y+n//3, n//3)
                divide(x+n//3, y+2*(n//3), n//3)
                divide(x+2*(n//3), y, n//3)
                divide(x+2*(n//3), y+n//3, n//3)
                divide(x+2*(n//3), y+2*(n//3), n//3)
                return
    
    if paper_data_type == 1:
        plus_data_cnt += 1
    elif paper_data_type == 0:
        zero_data_cnt += 1
    elif paper_data_type == -1:
        minus_data_cnt += 1

divide(0, 0, side)
print(minus_data_cnt)
print(zero_data_cnt)
print(plus_data_cnt)