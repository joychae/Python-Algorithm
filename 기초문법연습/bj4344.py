# 평균은 넘겠지 (1차원 배열 연습)
# 1회차 틀린문제 / 2회차 맞은 문제 64ms
# 1회차 - 로직은 맞았는데, 입력값 for문으로 여러줄 넣는걸 안해봐서 틀림

import sys

case = int(sys.stdin.readline().strip())

for i in range(case):
    input_value = list(map(int,sys.stdin.readline().strip().split()))
    student_cnt = input_value[0]
    scores = input_value[1:]

    scores_average = sum(scores)/student_cnt

    cnt = 0
    for score in scores:
        if score > scores_average:
            cnt += 1
    
    result = cnt/student_cnt
    print(f'{result*100:.3f}%')