# 균형잡힌 세상 (스택 연습)
# 1회차 틀린 문제 / 2회차 맞은 문제 104ms
# 1회차 때 공부한 모범답안보다 300ms 줄여서 푸는 데 성공했다. else문을 최대한 안써보려는 노력이 빛을 발했다!

import sys

while True:
    sentence = sys.stdin.readline()[:-1] # 습관적으로 sys.stdin.readline에 strip붙이는데, 제발 생각좀 하고 상황에 맞게 붙이자!
    bracket_stack = []
    ans = 1

    if sentence == ".":
        break

    for s in sentence:

        if s == "(":
            bracket_stack.append("(")
        elif s == ")":
            if bracket_stack and bracket_stack[-1] == "(":
                bracket_stack.pop()
            else:
                ans = 0
                print("no")
                break
        
        if s == "[":
            bracket_stack.append("[")
        elif s == "]":
            if bracket_stack and bracket_stack[-1] == "[":
                bracket_stack.pop()
            else:
                ans = 0
                print("no")
                break
    
    if ans and not bracket_stack:
        print("yes")
    
    elif ans and bracket_stack: # 맨 처음 검사 때 빼먹음 / 경우의 수 잘 생각할 것!
        print("no")


# 1회차 모범답안! : 내 답안은 104ms, 1회차때 참고한 모범담안 400ms / 최대한 else 안쓰려고 노력한 보람이 있다!

# while True:
#     bracket = input()
#     if bracket == ".":
#         break
#     bracket_stack = []
#     answer = True
    
#     for j in bracket:
#         if j == "(" or j == "[":
#             bracket_stack.append(j)
        
#         elif j == ")":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "(":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break
                
#         elif j == "]":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "[":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break

#     if answer == True and not bracket_stack:
#         print("yes")
#     else:
#         print("no")