# 바이러스 (DFS BFS 연습)
# 맞은 문제
# 짧게 푼 문제 찾아서 DFS 짧게 구현하는 법 익힐 필요 있음
import sys

# 그래프 만들기 (인접리스트로 구현) --> 이 방법 잘 외워두기
node = int(sys.stdin.readline().strip())
edge = int(sys.stdin.readline().strip())

adj = [[] for _ in range(node)]

for _ in range(edge):
    src, dest = map(int,sys.stdin.readline().strip().split())
    adj[src-1].append(dest)
    adj[dest-1].append(src)

# 인접리스트를 키 값을 가진 딕셔너리 형태로 변환, 이 과정 뺴고 해볼 수도 있겠음
adj_graph = dict()
for i in range(node):
    adj_graph[i+1] = adj[i]

# print(adj_graph)

# # DFS를 구현하는 함수식 만들기
def dfs_stack(adjacent_graph, start_node):
    # DFS 검사를 위한 stack, visited 리스트 만들기
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    # 중복제거를 위한 set, 자식노드끼리도 간선이 연결되어 있어서 중복이 발생
    return set(visited)

# print(dfs_stack(adj_graph, 1))
print(len(dfs_stack(adj_graph, 1))-1)