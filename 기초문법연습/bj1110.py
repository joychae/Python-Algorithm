# 더하기 사이클 (while문 연습)
# 1회차 틀린문제 / 2회차 맞은문제 64ms
# 1회차 - 데이터를 숫자로 가져가야 하는지, 문자열이나 리스트로 가져가야 하는지 잘 구분할 것.

import sys

original_num = int(sys.stdin.readline().strip())
fixed_original_num = original_num
result = 0
count = 0

while result != fixed_original_num: # 반복문은 탈출 조건을 꼭 가지고 있어야 한다.
    first_num = original_num%10
    second_num = (original_num//10 + original_num%10) % 10
    result = first_num*10 + second_num

    original_num = result
    count += 1

if original_num == 0:
    count += 1

print(count)