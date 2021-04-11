# 색종이 만들기 (분할정복 연습)
# 1회차 - 틀린 문제, 2회차 - 답안 참고해서 푼 문제 92ms
# 2회차 - 재귀함수 연습이 더 필요하다

import sys

side = int(sys.stdin.readline().strip())
color_list = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(side)]
white_color_cnt = 0
blue_color_cnt = 0

def divide(x, y, n):
    global white_color_cnt, blue_color_cnt
    paper_color = color_list[x][y]
    paper_color_check = 1

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper_color != color_list[i][j]:
                paper_color_check = 0
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                return
    
    if paper_color:
        blue_color_cnt += 1
    elif not paper_color:
        white_color_cnt += 1

divide(0, 0 , side)
print(white_color_cnt)
print(blue_color_cnt)
