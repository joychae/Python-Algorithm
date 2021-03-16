# 통계학
# 시간 초과...
# Counter 모듈 써서 맞음!

import sys
from collections import Counter

number_count = int(sys.stdin.readline().strip())
number_list = [int(sys.stdin.readline().strip()) for number in range(number_count)]

def average(number_list):
    return round(sum(number_list)/len(number_list))

def median(number_list):
    number_list.sort()
    return number_list[(len(number_list)//2)]

def mode(number_list):
    mode_list = Counter(number_list)
    order = mode_list.most_common()
    if len(order) != 1:
        if order[0][1] == order[1][1]:
            return order[1][0]
        else:
            return order[0][0]
    else:
        return order[0][0]
    
def range_interval(number_list):
    return max(number_list) - min(number_list)

print(average(number_list))
print(median(number_list))
print(mode(number_list))
print(range_interval(number_list))

# def mode(number_list):
#     number_list.sort()
#     mode_count_list = []
#     for i in range(len(number_list)):
#         mode_count_list.append(number_list.count(number_list[i]))
#     mode_count = max(mode_count_list)
#     mode_list = []
#     for number in number_list:
#         if number_list.count(number) == mode_count:
#             mode_list.append(number)
#     min_mode_number = min(mode_list)
#     mode_list = list(set(mode_list))
    
#     if len(mode_list) == 1:
#         print(*mode_list)
#     elif len(mode_list) != 1:
#         mode_list.remove(min_mode_number)
#         print(min(mode_list))