# 단어공부 (문자열 연습)
# 맞은 문제

from collections import Counter

word = list(input().lower())

reverse_dict = dict(map(reversed, Counter(word).items()))
valuelist = list(Counter(word).values())

max = max(valuelist)

if valuelist.count(max) == 1:
    print(reverse_dict.get(max).upper())
else:
    print("?")

# 다른풀이1

# words = input().upper()#words 받기
# alpabhet = list(set(words))# 집합에 넣음(중복 제거)
# #print(alpabhet)
# count_word = []#카운트 할 빈 리스트
# for word in alpabhet:#집합을 돌면서
#     count_word.append(words.count(word)) # 리스트의 원소들 따로 숫자 세기 (몰랐던 부분)
# print(count_word)
# if count_word.count(max(count_word))>=2:
#     print('?')
# else:
#     print(alpabhet[count_word.index(max(count_word))])#index (몰랐던 부분)

# # 다른풀이

# word = list(input().upper())          #['Z','Z','A']                  

# #set으로 받고 list로 받아야 함.. 아니면 인덱싱불가
# word_list = list(set(word))           #['Z','A']
 
# num_list=[]
# for i in word_list:             
#     num_list.append(word.count(i))     #[2,1]                  

# #새로운 리스트를 추가해 count가 동일한 인덱스를 가지게

# word_index=num_list.index(max(num_list))      #0
# if num_list.count(max(num_list))!=1:         # ex) num_list = [1,3,3,1]
#     print("?")                                # print(num_list.count(max(num_list)))
# else:
#     print(word_list[word_index])              #Z