# 토마토 (BFS 연습)
# 1회차 틀린 문제 / 2회차 틀린 문제
# 문제 특성을 충분히 생각못하고 특정 개념의 템플렛만 무작정 적용함.
# 중상 난이도 이상의 문제는 변형해 적용하는 유연함이 필요한 듯 하다.
# deque 모듈 코테에서 써도 괜찮으니, 잘 숙지해놓자
# 2회차 - DFS 에서만 재귀함수를 사용가능한데, BFS 에 대한 개념이 부족하다보니 재귀함수로 풀려하고 있었다. DFS BFS 헷갈리지 말자!
 
import sys
from collections import deque

garo, sero = map(int,sys.stdin.readline().strip().split())
tomatoes = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(sero)]
queue = deque() # bfs 탐색용 queue

for i in range(sero):
    for j in range(garo):
        if tomatoes[i][j] == 1:
            queue.append([i,j])

# 탐색을 위한 세팅
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 여기서부터 bfs

while queue:

    x, y = queue.popleft()

    for i in range(4):
        n_x = x + dx[i]  # 여기서는 x 가 세로값이다
        n_y = y + dy[i]

        if 0 <= n_x < sero and 0 <= n_y < garo and tomatoes[n_x][n_y] == 0:
            tomatoes[n_x][n_y] = tomatoes[x][y] + 1
            queue.append([n_x, n_y]) 

# bfs 끝 ----

result = 0
check_tomatoes = True
# print(tomatoes)

for i in tomatoes:
    for j in i:
        # print(j)
        if(j == 0):
            check_tomatoes = False
        result = max(result, j)

if not check_tomatoes:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result -1)