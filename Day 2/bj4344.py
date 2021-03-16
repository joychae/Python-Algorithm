# 평균은 넘겠지 (1차원 배열 연습)
# 틀린문제
# 로직은 맞았는데, 입력값 for문으로 여러줄 넣는걸 안해봐서 틀림

# import numpy as np

# list = input().split() # [ '5' , '5' , '5' ]
# intlist = [int(x) for x in list] # [ 5, 5, 5 ]

num = int(input())
for i in range(num): #이렇게 for 문 돌리면 입력값을 계속 넣으면서 동시에 계산되는 형태이다! 여러 줄을 넣어야 할 때는 for문 생각!
    intlist = list(map(int,input().split()))

    arForAverage = intlist[1:intlist[0]+1] # [ 5[0] , 50[1] , 50[2], 70[3], 80[4], 100[5]] [1:6] [0]
    sumForAverage = sum(arForAverage)
    quantity = intlist[0]

    Average = sumForAverage/quantity

    count = 0
    for i in arForAverage:
        if Average < i:
            count +=1

    result = count/quantity*100

    print(format(result,".3f")+"%")


# # 입력 출력 설정

# # 풀이1
# case = int(input())
# data = []
# for _ in range(case):
#     data= list(map(int,input().split()))
#     student = data[0] #데이터 첫번째 값을 빼거나, 인덱싱 하는 과정에서 애먹음,,
#     data.pop(0)# 첫 값 추출후 저장
#     avg = sum(data)/student # 평균 구해놓고
#     count = 0
#     for score in data:
#         if score > avg:
#             count += 1
#     rate = count/student*100
#     print(f"{'%.3f' % rate}%") # f"{'%.nf'%데이터}"

# # 풀이2
# num = int(input())
# for i in range(num):
#     student = list(map(int,input().split()))    #입력접근
#     s_average = sum(student[1:])/student[0]
    
#     pick = 0
#     for j in student[1:]:
#         if j>s_average:
#             pick+=1
    
#     per = pick/(len(student)-1)*100     #round함수 차이점
#     print(format(per,".3f")+"%")
#     print("{:.3f}".format(per)+"%")     #소수점 표현방식 2가지
