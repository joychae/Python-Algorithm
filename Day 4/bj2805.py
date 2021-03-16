# 나무 자르기(이분탐색)
# 틀린 문제
# while문 밖에 그릇들 만들고 적재적소에 넣어서 결과값 뽑는 부분이 미숙, 로직은 맞음

# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# left, right, ans = 0, max(a), 0
# while left <= right:
#     mid = (left + right) // 2
#     tree = 0
#     for i in range(n):
#         if mid < a[i]:
#             tree += a[i] - mid
#     if tree >= m:
#         ans = mid
#         left = mid + 1
#     elif tree < m:
#         right = mid - 1
# print(ans)

#  뭐가 다르길래!!! 내껀 안되냐 !!

# import sys

# N, M = map(int,sys.stdin.readline().split())
# trees = list(map(int,sys.stdin.readline().split()))

# # 반으로 자를 기준이 되는 H 값 구하기
# max_height = max(trees)

# H_left = 0
# H_right = max_height
# ans = 0

# while H_left <= H_right:

#     H =(H_left + H_right)//2

#     get = 0
#     for i in range(N):
#         if trees[i] > H:
#             get += trees[i] - H

#     if get >= M:
#         ans = H
#         H_left = H + 1
#     else:
#         H_right = H - 1
        
# print(ans)



# # 예전에 짠 코드

# import sys

# N, M = map(int,sys.stdin.readline().split())
# trees = list(map(int,sys.stdin.readline().split()))
# trees.sort()

# # 반으로 자를 기준이 되는 H 값 구하기
# # trees 마지막 index로 써도 됨
# max_height = max(trees)

# H_left = 0
# H_right = max_height

# while H_left <= H_right:
#     H =(H_left + H_right)//2
#     get_list =[]
#     for i in range(len(trees)-1):
#         if trees[i] > H:
#             get = trees[i] - H
#             get_list.append(get)

#     sum_get= sum(get_list)

#     if sum_get < M:
#         right = H -1
#     elif sum_get == M:
#         break
#     else:
        

# print(H)

# 다른풀이


import sys

N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

# 반으로 자를 기준이 되는 H 값 구하기
max_height = max(trees)

H_left = 0
H_right = max_height
ans = 0

while H_left <= H_right:

    H =(H_left + H_right)//2

    get_list =[]

    for i in range(len(trees)):
        if trees[i] > H:
            get = trees[i] - H
            get_list.append(get)
    sum_get= sum(get_list)

    if sum_get >= M:
        ans = H # 중요! 딱 그 값이 아니라 최적의 값을 찾아야 해서 그럼!!
        H_left = H + 1
    else:
        H_right = H - 1
        
print(ans)