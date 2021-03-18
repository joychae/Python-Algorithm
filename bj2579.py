# 계단오르기 (DP연습)
# 틀린 문제

# import sys

# n = int(sys.stdin.readline().strip())
# node = [int(sys.stdin.readline().strip()) for _ in range(n)]
# dp = [[0]]
# # print(node)

# for i in range(1, n+2):
#     # print(i)
#     node_accum = []
#     for j in range(i+1):
#         # print(j)

#         if j == 0:
#             if i-1 <= n-1:
#                 temp_node = dp[i-1][0]
#                 node_accum.append(temp_node + node[i-1])
#             else:
#                 break
        
#         elif 0 < j and j < i:
#             if i+j-1 <= n-1:
#                 temp_node = max(dp[i-1][j-1], dp[i-1][j])
#                 node_accum.append(temp_node + node[i+j-1])
#             else:
#                 dp.append(node_accum)
#                 break

#         elif j == i:
#             if 2*i-1 <= n-1:
#                 temp_node = dp[i-1][j-1]
#                 node_accum.append(temp_node + node[2*i-1])
#             else:
#                 dp.append(node_accum)
#                 break

#     dp.append(node_accum)
#     print(node_accum)

import sys

n = int(input())
stair = [0]*301
dp = [0]*301

for i in range(n):
    stair[i] = int(input())
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stair[i - 1], dp[i - 2]) + stair[i]
print(dp[n - 1])