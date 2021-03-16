# 토마토 (DFS BFS 연습)
# 틀린 문제
# 문제 특성을 충분히 생각못하고 특정 개념의 템플렛만 무작정 적용함.
# 중상 난이도 이상의 문제는 변형해 적용하는 유연함이 필요한 듯 하다.

# deque 모듈 코테에서 써도 괜찮으니, 잘 숙지해놓자

import sys

M, N = map(int,sys.stdin.readline().strip().split())

# BFS 문제의 기본은 노드갯수, 간선갯수, 각 간선의 양끝노드 구하기부터 시작한다.
node = M * N
edge = M*(N-1) + (M-1)*N

tomatoes = [sys.stdin.readline().strip().split() for t in range(N)]

edges = []
# # 가로 연결선 구하기
for i in range(1, node):
    h_edge = [i, i + 1]
    if (h_edge[0])%M != 0:
        edges.append(h_edge)

# 세로 연결선 구하기
for i in range(1, node-M+1):
    v_edge = [i, i + M]
    edges.append(v_edge)

# 빠지는 노드, 시작 노드 구하기
deletes = []
starts = []
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == "-1":
            del_node = M*i + (j+1)
            deletes.append(del_node)
        if tomatoes[i][j] == "1":
            start_node = M*i + (j+1)
            starts.append(start_node)

for del_node in deletes:
    edges = [i for i in edges if not del_node in i]

# 인접 그래프 만들기
adj = [[] for _ in range(1, node+1)]

for i in range(0, len(edges)): # 디버깅 결과 여기서 이상해짐
    src = edges[i][0]
    dest = edges[i][1]
    adj[src-1].append(dest)
    adj[dest-1].append(src)

# 인접 그래프 딕셔너리로 치환
adj_graph = dict()
for i in range(node):
    adj_graph[i+1] = adj[i]

#BFS 함수
#갔던 곳은 다시는 안가주는 로직이 필요한데...
def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []
    count = 0 # 갯수세기용으로 추가

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        count += 1
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)
    return set(visited)
    # return count

# 함수 적용
for start_node in starts:
    print(bfs_queue(adj_graph,start_node))