# 소수구하기(기본 수학)
# 틀린문제

# # 시간초과 풀이

# import sys
# import math

# M, N = map(int,sys.stdin.readline().strip().split())

# def find_prime_number(M,N):
#     prime_list =[]
#     for i in range(2, N+1):
#         for j in prime_list:
#             if i%j == 0 and j*j <= i:
#                 break
#         else: # else 구문을 이렇게 if 랑 다른 층위에 만드는 상황들은?
#             prime_list.append(i)
#     return prime_list
# result = find_prime_number(M,N)
# print(result)


# 에라토스테네스의 체 - 위보다 빠름
m, n = map(int, input().split())
array = [True for i in range(1000001)]  # 모든 수가 소수인것으로 초기화
array[1] = 0  # 1은 소수가 아님
# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인
    if array[i] == True:  # i 가 소수인경우
        # i를 제외한 i의 모든 배수 제거
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
# M부터 N까지의 모든 소수 출력
for i in range(m, n+1):
    if array[i]:
        print(i)





# # 새로운 풀이

# import math
# import numpy as np

# M, N = map(int,input())

# list =np.array([])
# for i in range(M, N+1):
#     list.append(i)

# for j in range(2, len(list)):
#     if list%j == 0:
#         list.remove(i)
#         break
#     if i in list:
#         print(i)

