# 회전하는 큐 (큐 연습)
# 틀린 문제

import sys
import math

N, M = map(int,sys.stdin.readline().strip().split())
find_num = list(map(int,sys.stdin.readline().strip().split()))

list = [n+1 for n in range(N)] # [ 1, 2, ... , 10]
count = 0

for i in range(M):

    if find_num[i] == list[0]:
        list.pop(0)

    elif list.index(find_num[i]) <= math.ceil(len(list)/2):
        for j in range(list.index(find_num[i])):
            delete_num = list[0]
            count += 1
            list.pop(0)
            list.append(delete_num)

            if find_num[i] == list[0]: # i 인덱스를 가진 수가 list의 첫 수와 동일하면
                list.pop(0)
        
    else:
        for j in range(len(list) - list.index(find_num[i])-1):
            delete_num = list[-1]
            count += 1
            list.pop()
            list.insert(0, delete_num)

            if find_num[i] == list[-1]: # i 인덱스를 가진 수가 list의 첫 수와 동일하면
                list.pop()
                count += 1

print(list)
print(count)