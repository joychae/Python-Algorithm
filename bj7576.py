# 토마토 (DFS BFS 연습)
# 틀린 문제
# 문제 특성을 충분히 생각못하고 특정 개념의 템플렛만 무작정 적용함.
# 중상 난이도 이상의 문제는 변형해 적용하는 유연함이 필요한 듯 하다.

# deque 모듈 코테에서 써도 괜찮으니, 잘 숙지해놓자

import sys

input = sys.stdin.readline

def bfs(matrix, x, y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if n_x >= 0 and n_x < N and n_y >= 0 and n_y < N:
            if matrix[n_x][n_y] == 0:
                matrix[n_x][n_y] = matrix[x][y] + 1
                print(matrix)
                matrix = bfs(matrix, n_x, n_y)
    return matrix

M, N = map(int,input().strip().split())
matrix = [list(map(int,input().strip().split())) for _ in range(N)]

ans = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            ans.append(bfs(matrix, i, j))
print(ans)