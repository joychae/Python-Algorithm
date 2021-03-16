# 좌표 정렬하기2 (정렬)
# 맞은 문제

import sys

case = int(sys.stdin.readline().strip())

# 2차원 리스트 만들기
points = []
for point in range(case):
    x, y = map(int,sys.stdin.readline().strip().split())
    point = [x, y]
    points.append(point)

# x 값 순서로 정렬
points.sort(key = lambda x: (x[1], x[0]))

# 출력
for i, j in points:
    print(i, j)