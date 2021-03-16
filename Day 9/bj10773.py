# 제로 (스택 연습)
# 맞은 문제
# 코드효율화 해보자 (else 뺴기)

import sys

K = int(sys.stdin.readline().strip())

stack = []

for i in range(K):
    num = int(sys.stdin.readline().strip())

    if num == 0:
        stack.pop()
    
    else:
        stack.append(num)

print(sum(stack))

# # 다른 풀이

# import sys

# K = int(sys.stdin.readline().strip())

# stack = []

# for i in range(K):
#     num = int(sys.stdin.readline().strip())

#     if num == 0:
#         stack.pop()
#         continue
    
#     stack.append(num)

# print(sum(stack))