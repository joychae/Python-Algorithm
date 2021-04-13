# 크로아티아 알파벳 (문자열 연습)
# 맞은 문제

# import sys

# word = sys.stdin.readline().strip()
# wordlength = len(list(word))

# alphabet_2 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# search_2 = sum([word.count(s) for s in alphabet_2])
# search_3 = word.count('dz=')

# # result = wordlength - search_2*2 - (search_3)*3 + search_2 +search_3+ search_3*2
# result = wordlength - search_2
# print(result)

# # search_3 변수 지워보자 // 이래도 맞네

import sys

word = sys.stdin.readline().strip()
wordlength = len(list(word))

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

search = sum([word.count(s) for s in alphabet])

result = wordlength - search
print(result)


# # 다른 풀이 - replace 사용해서 문자열을 변환하는 방법으로 품

# word = input()
# alphabet = ['c-','dz=','c=','d-','lj','nj','s=','z=']     #돌아가는 순서!!!

# for i in alphabet:
#     if i in word:
#         word=word.replace(i,"!")             # word.replace(a,b)   aaa bbb
        

# print(len(word))