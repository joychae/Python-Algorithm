# 별 찍기 - 10
# 맞은 문제 1944ms
# 주의할 점 - point_list 2차원 배열 만들 때 [['*']*side]*side 하면 얕은 복사 되서 참조값이 같아진다. 곱하기 초기화는 주의해서 쓰자!

import sys

side = int(sys.stdin.readline().strip())
point_list = [['*']*side for _ in range(side)]

def point(x, y, n):
    global point_list

    if n >= 3:
        point(x, y, n//3)
        point(x, y+n//3, n//3)
        point(x, y+2*(n//3), n//3)
        point(x+n//3, y, n//3)
        point(x+n//3, y+n//3, n//3) # 비어있는 칸
        point(x+n//3, y+2*(n//3), n//3)
        point(x+2*(n//3), y, n//3)
        point(x+2*(n//3), y+n//3, n//3)
        point(x+2*(n//3), y+2*(n//3), n//3)
        
        for i in range(x+n//3, x+2*(n//3)):
            for j in range(y+n//3, y+2*(n//3)):
                point_list[i][j] = ' '

    return point_list

for line in point(0, 0, side):
    print(''.join(line))