
import sys

N = int(sys.stdin.readline().strip())
paper_list = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
white_count = 0
blue_count = 0

def divide(x, y, n):
    global white_count, blue_count
    paper_color = paper_list[x][y]
    check_color = True

    for i in range(x,x+n):
        if not check_color: # 이거 왜 있을까?
            break
        for j in range(y,y+n):
            if paper_color != paper_list[i][j]:
                check_color = False
                divide(x, y, n//2)
                divide(x, y+(n//2), n//2)
                divide(x+(n//2), y, n//2)
                divide(x+(n//2), y+(n//2), n//2)
                break
    
    if check_color:
        if paper_color:
            blue_count += 1
        elif not paper_color:
            white_count += 1

divide(0, 0, n)
print(white_count)
print(blue_count)

# def divide(N, paper_list):
#     left_slice = [row[0:N//2] for row in paper_list]
#     right_slice = [row[N//2:N+1] for row in paper_list]
#     paper_1 = left_slice[0:N//2]
#     paper_2 = right_slice[0:N//2]
#     paper_3 = left_slice[N//2:N+1]
#     paper_4 = right_slice[N//2:N+1]

#     return paper_1, paper_2, paper_3, paper_4

# count_blue = 0
# count_white = 0

# while True:
#     paper_list_1 = divide(N, paper_list)[0]
#     # paper_list_2 = divide(N, paper_list)[1]
#     # paper_list_3 = divide(N, paper_list)[2]
#     # paper_list_4 = divide(N, paper_list)[3]

#     if 1 and 0 in paper_list_1:
#         divide(N//2, paper_list_1)
#     else:
#         if 1 in paper_list_1:
#             count_blue += 1
#             break
#         elif 0 in paper_list_1:
#             count_white +=1
#             break
#     N = N//2
#     if len(paper_list_1) == 1:
#         if 1 in paper_list_1:
#             count_blue +=1
#         elif 0 in paper_list_1:
#             count_white += 1
#         break

# print(paper_list_1)
# print(count_white, count_blue)

import sys
n=int(sys.stdin.readline())
 
color_paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]#x행 y열
 
white=0#0이면 흰생
blue=0#1이면 파란색
 
def cut(x,y,n):
    global blue,white
    check=color_paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=color_paper[i][j]:#하나라도 같은색이 아니라면
                #4등분
                cut(x,y,n//2)#1사분면
                cut(x,y+n//2,n//2)#2사분면
                cut(x+n//2,y,n//2)#3사분면
                cut(x+n//2,y+n//2,n//2)#4사분면
                return
 
    if check==0:#모두 흰색일때
        white+=1
        return
    else:   #모두 파란색일때
        blue+=1
        return
 
 
cut(0,0,n)
print(white)
print(blue)

