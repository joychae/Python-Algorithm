# 달팽이는 올라가고 싶다
# 틀린문제

import sys

A, B, V = map(int,sys.stdin.readline().split())

count = 0

for i in range(V//A-B):
    reverse_V = V-((A-B)*i)

    if reverse_V + A = V:
        break

    if reverse_V + A < V:
        break
    
    count += 1
    

result = V//(A-B)- count + 1

print(result)



# V 커지면 무한루프 엄청 돌아서 다른 방법 찾아야 함
# distance = 0
# count = 0

# while True:
#     distance += A
#     if distance >= V:
#         count += 1
#         print(count)
#         break;
#     else:
#         distance -= B
#         count += 1


# import sys

# A, B, V = map(int,sys.stdin.readline().split())

# count = 0

# for i in range(V//A-B):
#     reverse_V = V-((A-B)*i)
#     if reverse_V + A < V:
#         break
#     count += 1

# result = V//(A-B)- count + 1

# print(result)
