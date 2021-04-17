# 유기농 배추 (dfs 연습)
# 1회차 맞은 문제 84ms
# 백준에서 recursion error 가 떠서 sys 모듈 활용해 recursion limit 풀어주니 바로 정답이었다
# 실전에서는 이러면 bfs 로 풀어보는 시도를 해야 할 듯 하다.
# 다음에 풀 때는 bfs 로 풀어보자

import sys

sys.setrecursionlimit(10000)
case = int(sys.stdin.readline().strip())

def dfs(matrix, cnt, x, y):
    matrix[x][y] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if 0 <= n_x < sero and 0 <= n_y < garo and matrix[n_x][n_y] == 1:
           cnt = dfs(matrix, cnt+1, n_x, n_y)
    
    return cnt

for _ in range(case):
    garo, sero, baechu_cnt = map(int, sys.stdin.readline().strip().split())
    baechu_list = [[0]*garo for _ in range(sero)]

    for i in range(baechu_cnt):
        x, y = map(int,sys.stdin.readline().strip().split())
        baechu_list[y][x] = 1

    ans = []
    for i in range(sero):
        for j in range(garo):
            if baechu_list[i][j] == 1:
                ans.append(dfs(baechu_list, 1, i, j))

    ans.sort()
    print(len(ans))