import sys

array_q = int(sys.stdin.readline().strip())
array_list = list(map(int,sys.stdin.readline().strip().split()))
array_list.sort()
target_q = int(sys.stdin.readline().strip())
target_list = list(map(int,sys.stdin.readline().strip().split()))

def binary(target,array):
    min_idx = 0
    max_idx = len(array)-1
    mid_idx = (min_idx + max_idx)//2

    while min_idx <= max_idx:
        if target == array[mid_idx]:
            return 1
        elif target > array[mid_idx]:
            min_idx = mid_idx + 1
        elif target < array[mid_idx]:
            max_idx = mid_idx - 1
        mid_idx = (min_idx + max_idx)//2
    return 0
    
for i in target_list:
    print(binary(i,array_list))