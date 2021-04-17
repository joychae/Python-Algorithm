# 단지번호 붙이기 (dfs 연습)
# 1회차 - 힌트 참고해서 푼 문제

import sys

side = int(sys.stdin.readline().strip())
houses = [list(map(int,sys.stdin.readline().strip())) for _ in range(side)]

def dfs(matrix, cnt, x, y):
    matrix[x][y] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if 0 <= n_x < side and 0 <= n_y < side and matrix[n_x][n_y] == 1:
           cnt = dfs(matrix, cnt+1, n_x, n_y)
    
    return cnt
    
ans = []
for i in range(side):
    for j in range(side):
        if houses[i][j] == 1:
            ans.append(dfs(houses, 1, i, j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)