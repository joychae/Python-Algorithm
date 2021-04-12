# 수 찾기
# 1회차 맞은 문제 588ms / 2회차 맞은 문제 876ms
# min, max 실수가 아직도 잦다..

import sys

q_cnt = int(sys.stdin.readline().strip())
q_array = list(map(int,sys.stdin.readline().strip().split()))
q_array.sort()
target_cnt = int(sys.stdin.readline().strip())
target_array = list(map(int,sys.stdin.readline().strip().split()))

for target in target_array:
    min_idx = 0
    max_idx = len(q_array)-1
    mid_idx = (min_idx + max_idx)//2
    result = 0

    while min_idx <= max_idx:
        if q_array[mid_idx] == target:
            result = 1
            break
        elif q_array[mid_idx] < target:
            min_idx = mid_idx + 1
        elif q_array[mid_idx] > target:
            max_idx = mid_idx - 1
        mid_idx = (min_idx + max_idx)//2
    
    print(result)

# 1회차 답안

# import sys

# array_q = int(sys.stdin.readline().strip())
# array_list = list(map(int,sys.stdin.readline().strip().split()))
# array_list.sort()
# target_q = int(sys.stdin.readline().strip())
# target_list = list(map(int,sys.stdin.readline().strip().split()))

# def binary(target,array):
#     min_idx = 0
#     max_idx = len(array)-1
#     mid_idx = (min_idx + max_idx)//2

#     while min_idx <= max_idx:
#         if target == array[mid_idx]:
#             return 1
#         elif target > array[mid_idx]:
#             min_idx = mid_idx + 1
#         elif target < array[mid_idx]:
#             max_idx = mid_idx - 1
#         mid_idx = (min_idx + max_idx)//2
#     return 0
    
# for i in target_list:
#     print(binary(i,array_list))