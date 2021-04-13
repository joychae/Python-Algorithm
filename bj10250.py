# ACM 호텔 (기본 수학)
# 맞은 문제

import sys
import math

test_data = int(sys.stdin.readline().strip())
for test in range(test_data):
    H , W , N = map(int,sys.stdin.readline().strip().split())

    if N % H != 0:
        h = N % H
        w = math.ceil(N/H)
    else:
        h = H
        w = N//H
    
    h = str(h)

    if w <10:
        w = "0" + str(w)
    else:
        w = str(w)

    result = h + w

    print(result)

# # 풀이 2

# import sys

# test_data = int(sys.stdin.readline().strip())
# for test in range(test_data):
#     H , W , N = map(int,sys.stdin.readline().strip().split())

#     if N % H != 0:
#         h = N % H
#         for w in range(1,99):
#             if w*H > N:
#                 break

#     else:
#         h = H
#         w = N//H

#     h = str(h)

#     if w <10:
#         w = "0" + str(w)
#     else:
#         w = str(w)

#     result = h + w

#     print(result)