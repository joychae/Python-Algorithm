# 전자레인지 (그리디 알고리즘 연습)
# 1회차 맞은문제 72ms

import sys

total_sec = int(sys.stdin.readline().strip())
buttons = [300, 60, 10]
buttons_cnt = []

for button in buttons:
    temp_total_sec = total_sec%button
    button_cnt = total_sec//button
    buttons_cnt.append(button_cnt)
    total_sec = temp_total_sec

if total_sec == 0:
    print(*buttons_cnt)
elif total_sec != 0:
    print(-1)