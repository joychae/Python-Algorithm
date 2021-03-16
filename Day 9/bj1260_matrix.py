from sys import stdin
N, M, start = map(int, stdin.readline().split())
graph       = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    x, y = map(int, stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

# dfs -> stack 이용
def dfs(start):                                
    visited = []
    stack   = [start]
    while stack:
        pop = stack.pop()
        if pop not in visited:
            visited.append(pop)
            for number in range(N, -1, -1):
                if graph[pop][number] ==  1:
                    stack.append(number)
    for i in visited:
        print(i, end=" ")
    
def bfs(start):
    visited = []
    queue   = [start]
    while queue:
        pop = queue.pop(0)
        if pop not in visited:
            visited.append(pop)
            for number in range(1, N+1):
                if graph[pop][number] ==  1:
                    queue.append(number)
    for i in visited:
        print(i, end=" ")

dfs(start)
print()
bfs(start)