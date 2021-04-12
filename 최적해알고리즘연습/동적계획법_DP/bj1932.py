# 정수삼각형 (DP 연습)
# 1회차 맞은 문제 (RGB거리 문제와 유사) / 2회차 맞은 문제 188ms
# 디버깅 하느라 죽을뻔한 문제... 이중 for 문 쓸때 리스트 초기화, i 쓰는거 주의 해서 쓰자!!

import sys

size = int(sys.stdin.readline().strip())
number_list = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(size)]
dp = [number_list[0]]

for i in range(1,size):
    temp_number_list = [0]*len(number_list[i])
    for j in range(len(number_list[i])):
        if j == 0:
            temp_number_list[0] = dp[i-1][0] + number_list[i][0]
        elif j > 0 and j <len(number_list[i])-1:
            temp_number_list[j] = max(dp[i-1][j-1], dp[i-1][j]) + number_list[i][j]
        elif j == len(number_list[i])-1:
            temp_number_list[j] = dp[i-1][j-1] + number_list[i][j]
    dp.append(temp_number_list)

print(max(dp[size-1]))


# import sys

# n = int(sys.stdin.readline().strip())
# node_number = []

# for _ in range(n):
#     node_number.append(list(map(int,sys.stdin.readline().strip().split())))

#     dp = [node_number[0]]

# # print(dp)
# print(node_number)

# for i in range(1, n):
#     # print(i)
#     node_accum = []
#     for j in range(i+1):
#         # print(j)

#         if j == 0:
#             temp_node = dp[i-1][0]
#             node_accum.append(temp_node + node_number[i][0])
        
#         elif 0 < j and j < i:
#             temp_node = max(dp[i-1][j-1], dp[i-1][j])
#             node_accum.append(temp_node + node_number[i][j])
        
#         else:
#             temp_node = dp[i-1][j-1]
#             node_accum.append(temp_node + node_number[i][i])

#     dp.append(node_accum)

# print(max(dp[n-1]))