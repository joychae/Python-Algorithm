# 그룹 단어 체커 (문자열 연습)
# 맞은 문제

import sys

# 입력값 받는 수식
case = int(sys.stdin.readline().strip())
words = [list(sys.stdin.readline().strip()) for _ in range(case)]

# 그룹 단어 판별 함수식
def groupNumber(word):

    for i in range(len(word)-1):

        if word[i] == word[i+1]:
            continue

        else:
            for j in range(i+1,len(word)):

                if word[i] == word[j]:
                    return False
                    break
    
    return True

# 결과 출력식
count = 0
for w in words:
    result = groupNumber(w)
    if result is True:
        count += 1

print(count)