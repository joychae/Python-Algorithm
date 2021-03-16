# 균형잡힌 세상 (스택 연습)
# 틀린 문제

# import sys

# while True:
#     sentence = [s for s in sys.stdin.readline().strip()]
#     answer = True

#     def findBalance(sentence):
#         for i in range(len(sentence)-1):
#             if sentence[i] == "]":
#                 for j in range (i-1, -1, -1):
#                     if sentence[j] == "(":
#                         answer = False
#                         break
#                     elif sentence[j] == "[":
#                         answer = True
#                         break
#                     else:
#                         if j == 0:
#                             answer = False
#                             break
#                         else:
#                             pass

#     def findBalance2(sentence):
#         for i in range(len(sentence)-1):
#             if sentence[i] == ")":
#                 for j in range (i-1, -1, -1):
#                     if sentence[j] == "[":
#                         answer = False
#                         break
#                     elif sentence[j] == "(":
#                         answer = True
#                         break
#                     else:
#                         if j == 0:
#                             answer = False
#                             break
#                         else:
#                             pass

#     if answer == True:
#         print("yes")
#     else:
#         print("no")
    
#     if sentence == ["."]:
#         break
    



# # 임시 저장 코드

# import sys

# sentence = [s for s in sys.stdin.readline().strip()]

# list = []
# ans = 0
# ans2 =0

# for i in range(len(sentence)-1):
#     if sentence[i] == "]":
#         # ans = i
#         for j in range (i-1, -1, -1):
#             if sentence[j] == "(":
#                 # ans2 = j
#                 print("no")
#                 break
#             elif sentence[j] == "[":
#                 # ans2 = j
#                 print("yes")
#                 break
#             else:
#                 pass

# for i in range(len(sentence)-1):
#     if sentence[i] == ")":
#         # ans = i
#         for j in range (i-1, -1, -1):
#             if sentence[j] == "[":
#                 # ans2 = j
#                 print("no")
#                 break
#             elif sentence[j] == "(":
#                 # ans2 = j
#                 print("yes")
#                 break
#             else:
#                 pass

# print(ans)
# print(ans2)

# 모범답안!

while True:
    bracket = input()
    if bracket == ".":
        break
    bracket_stack = []
    answer = True
    
    for j in bracket:
        if j == "(" or j == "[":
            bracket_stack.append(j)
        
        elif j == ")":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "(":
                bracket_stack.pop()
            else:
                answer = False
                break
                
        elif j == "]":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "[":
                bracket_stack.pop()
            else:
                answer = False
                break

    if answer == True and not bracket_stack:
        print("yes")
    else:
        print("no")