# DFS와 BFS (DFS, BFS 연습문제)
# 틀린 문제 (완전 이진 트리의 DFS, BFS 의 구현 방법만 알고 있었음)

import sys
from collections import deque

node, edge, start_node = map(int,sys.stdin.readline().strip().split())

adj_list = [[] for _ in range(node)] # 인접그래프 만들기

for _ in range(edge):
    src, dest = map(int,sys.stdin.readline().strip().split())
    adj_list[src-1].append(dest)
    adj_list[dest-1].append(src)

adj_graph = dict()
for i in range(node):
    adj_graph[i+1] = adj_list[i]

def dfs(adj_graph, start_node): # DFS 함수식 구현
    stack = [start_node]
    visited = []

    while stack:
        visit_node = stack.pop()
        
        if visit_node not in visited:
            visited.append(visit_node)
            adj_graph[visit_node].sort(reverse=True)
            
            for adj_node in adj_graph[visit_node]:
                if adj_node not in visited:
                    stack.append(adj_node)
    
    return visited

def bfs(adj_graph, start_node):
    q = deque()
    q.append(start_node)
    visited = []

    while q:
        visit_node = q.popleft()

        if visit_node not in visited:
            visited.append(visit_node)
            adj_graph[visit_node].sort()

            for adj_node in adj_graph[visit_node]:
                if adj_node not in visited:
                    q.append(adj_node)

    return visited

print(*dfs(adj_graph, start_node))
print(*bfs(adj_graph, start_node))



