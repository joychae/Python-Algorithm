# 베르트랑 공준 (기본수학2 연습)
# 맞은 답안
# PyPy로 제출했을 때만 정답처리 됨... 소수 구하기 관련 더 효율적인 로직 만들어놓을 필요 있음

import sys
import math

# 모든 수가 소수인것으로 초기화 , 1은 소수가 아님
array = [1] * 246913
array[0] = 0
array[1] = 1

# 에라토스테네스의 체
# 2부터 n의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(246912)) + 1): 
        
# i 가 소수인경우
    if array[i] ==1: 
        # i를 제외한 i의 모든 배수 제거
        for j in range(i*i, 246913, i):
            array[j] = 0


# 원하는 범위 만큼 구해놓은 소수 정렬을 잘라주기
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    print(sum(array[n+1:2*n+1]))


# # 효율화 전

# import sys
# import math

# while True:
#     n = int(sys.stdin.readline().strip())
#     if n == 0:
#         break

#     # 모든 수가 소수인것으로 초기화 , 1은 소수가 아님
#     array = [True for i in range(2*n+1)]
#     array[1] = False

#     # 에라토스테네스의 체
#     for i in range(2, int(math.sqrt(2*n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인
        
#         # i 가 소수인경우
#         if array[i] == True: 
#             # i를 제외한 i의 모든 배수 제거
#             j = 2
#             while i * j <= 2*n:
#                 array[i*j] = False
#                 j += 1

#     # 원하는 범위 만큼 구해놓은 소수 정렬을 잘라주기
#     count = 0
#     for i in range(n+1, (n*2)+1):
#         if array[i]:
#             count +=1
#     print(count)
