# 쿼드트리
# 1회차 틀린문제 / 2회차 틀린문제

import sys

side = int(sys.stdin.readline().strip())
color_list = [list(sys.stdin.readline().strip()) for _ in range(side)]

def divide(x, y, n):
    dot_color = color_list[x][y]
    compress_list = []

    for i in range(x, x+n):
        for j in range(y, y+n):
            if dot_color != color_list[i][j]:
                compress_list.append('(')
                compress_list.extend(divide(x, y, n//2))
                compress_list.extend(divide(x, y+n//2, n//2))
                compress_list.extend(divide(x+n//2, y, n//2))
                compress_list.extend(divide(x+n//2, y+n//2, n//2))
                compress_list.append(')')
                return compress_list

    return str(color_list[x][y])

print(''.join(divide(0, 0, side)))