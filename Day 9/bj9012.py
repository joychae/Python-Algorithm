# 괄호 (스택 연습)
# 맞은 문제 (하지만 오답노트 필요...)
# 스택은 짝짓기 문제에서 유용하게 활용될 수 있다는 점 기억!

import sys

case = int(sys.stdin.readline().strip())

for _ in range(case):
    stack = []
    answer = True
    arr = sys.stdin.readline().strip()
    replace_arr = arr.replace("(","u")
    replace_arr = replace_arr.replace(")","v")
    replace_arr = str(replace_arr)

    for j in range(len(arr)):

        if replace_arr[j] == "u":
            stack.append("u")
        
        elif replace_arr[j] == "v":
            if stack:
                stack.pop()
            else:
                answer = False
                break
    
    if answer and not stack: # 이 부분에서 많이 헤매었음 #맨 처음에 불린 값 넣어두고 False 만 바꾸는 스킬 연습 필요
        print("YES")
    
    else:
        print("NO")