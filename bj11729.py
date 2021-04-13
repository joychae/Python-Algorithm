# 하노이 탑 이동 순서 (재귀 연습)
# 틀린 문제
# 아직도 재귀함수는 너무 어렵다...

n = int(input())

def move(num, x, y): # ( x, 6 -x -y, y) x기둥에 쌓인 원반 num개를 y기둥에 옮깁니다.
    if num > 1:
        move(num-1, x, 6-x-y)

    print(x, y)

    if num > 1:
        move(num-1, 6-x-y, y)

print(2**n -1)
move(n, 1, 3)

# # 다른풀이

# input = int(input())
# def hanoi(num, start, via, dest):
#     if num == 0:
#         return
#     else:
#         hanoi(num-1, start, dest, via)
#         print(start, dest)
#         hanoi(num-1, via, start, dest)
#     return True
# hanoi(input, 1, 2, 3)