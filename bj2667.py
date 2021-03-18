import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

def dfs(matrix, cnt, x,y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        # 이 근처 다 n_x, n_y로 간다.
        if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
            # 범위 check
            if matrix[n_x][n_y]==1:
            # 그부분이 1이면
                cnt = dfs(matrix, cnt+1, n_x, n_y)
                # cnt를 증가시켜서 다시한번 그 근처 확인
    return cnt
    # 다 cnt검사하면 끝을 낸다.

matrix = [list(map(int, list(read()))) for _ in range(n)]
# matrix에 input값 넣기

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            일단 1로 뭔가의 그룹이다.
            ans.append(dfs(matrix, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)

# # 중간 저장

# import copy
# from collections import deque


# N = int(input())
# box = [list(input()) for _ in range(N)]
# ripen_box = copy.deepcopy(box) #같은 리스트를 하나 더 생성(안해도 상관 없음)
# visited = []
# queue = deque() #일반 리스트로 큐를 구현하면 시간이 너무 오래걸린다


# for i in range(N):
#     for j in range(N):
#         if box[i][j] == "1" and [i, j] not in visited:
#             queue.append([i, j])
#             break #이미 익어있는 토마토 위치를 큐에 넣어줌

# while queue:
#     current = queue.popleft()
#     [i, j] = current #하나씩 빼면서 비교
#     visited.append(current)

#     #위
#     if i > 0 and ripen_box[i-1][j] == "1":
#         queue.append([i-1, j]) #큐에 넣고
#         ripen_box[i-1][j] = "5" #하루 더 기다려야하니, 1을 더해준다.
        
#     #아래
#     if i < N-1 and ripen_box[i+1][j] == "1":
#         queue.append([i+1, j])
#         ripen_box[i+1][j] = "5"
    
#     #왼쪽
#     if j > 0 and ripen_box[i][j-1] == "1":
#         queue.append([i, j-1])
#         ripen_box[i][j-1] = "5"
    
#     #오른쪽
#     if j < N-1 and ripen_box[i][j+1] == "1":
#         queue.append([i, j+1])
#         ripen_box[i][j+1] = "5"
        
# count = 0
# for row in ripen_box:
#     count += row.count("5")
# print(count)
# print(visited)

# a = '1 2 3 4 5 6'
# # a = list(a)
# # a = list(map(int,list(a)))
# a = list(map(int,a.split))

# # a = 123456
# # a = list(a)
# print(a)