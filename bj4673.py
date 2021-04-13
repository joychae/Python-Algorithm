# 셀프 넘버(함수 연습)
# 맞은 문제

# # 중간에 반복문을 list 형태로 append 해주기 위한 빈 리스트 생성
# list=[]

# for n in range(1,10000):
#     def d(n):
#         # 숫자 자릿수별로 다른 수식을 적용해야 함
#         # if n < 100:
#         #     return n + n//10 + n%10
#         # elif 100 <= n <1000:
#         #     return n + n//100 + (n//10)%10 + n%10
#         # else:
#         return n + n//1000 + (n//100)%10 + (n//10)%10 + n%10

#     # 반복문 리스트에 넣어주기 (반복문을 리스트로 변환하는 작업)
#     list.append(d(n))

# for n in range(1,10000):
#     # 리스트에 없는 함수 불러오기
#     Result = n in list
#     if Result is False:
#         print(n)



# # 수정후

list=[]

for n in range(1,10000):
    def d(n):
        return n + n//1000 + (n//100)%10 + (n//10)%10 + n%10
    list.append(d(n))

for n in range(1,10000):
    # 리스트에 없는 함수 불러오기
    Result = n in list
    if Result is False:
        print(n)


# 풀이1
# # n_list=[]
# # for i in range(0,10000):
# #     n_list.append(i+sum(list(map(int,str(i)))))                  
# # print(n_list)

# int(x) for x in list

# n_list=[]
# for i in range(0,10000):
#     n_list.append(i+sum(list(map(int,str(i)))))                  
# print(n_list)

n_list = [i+sum(list(map(int,str(i)))) for i in range(0,10000)]  #int를 바로 list로 넣으려면 다시 리스트를 만들어야한다?

for i in range(0,10001):
    if i not in n_list:
        print(i)

# # 풀이2
# def self_num_check(n):
#     return n + n//1000 + n//100%10 + n//10%10 + n%10
#     # return n + n//10 + n%10
# create_num = []
# # array = [i for i in range(100)]
# array = [i for i in range(10000)]
# self_num=[]
# # for i in range(100):
# for i in range(10000):
#     # print(self_num_check(i))
#     # if self_num_check(i) < 100:
#     if self_num_check(i) < 10000:
#         print(self_num_check(i))
#         create_num.append(self_num_check(i))
        
# self_num=list(set(array)-set(create_num))
# self_num = sorted(self_num)
# for i in self_num:
#     print(i)
