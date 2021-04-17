# 미로 탐색 (bfs 연습)
# 1회차 맞은 문제 124ms

import sys
from collections import deque

sero, garo = map(int,sys.stdin.readline().strip().split())
miro = [list(map(int,sys.stdin.readline().strip())) for _ in range(sero)]
queue = deque()
queue.append([0, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if 0 <= n_x < sero and 0 <= n_y < garo and miro[n_x][n_y] == 1 :
            miro[n_x][n_y] = miro[x][y] + 1
            queue.append([n_x, n_y])

print(miro[sero-1][garo-1])