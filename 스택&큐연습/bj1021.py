# 회전하는 큐 (큐 연습)
# 1회차 틀린 문제 / 2회차 맞은 문제 92ms
# 2회차 - q.append(q.popleft()) 이렇게 써도 q에서 제일 왼쪽 요소가 제거되고, 붙여진다는 개념을 잘 숙지했기 때문에 쉽게 해결 가능했다.

import sys
from collections import deque # 덱은 시간복잡도를 위해 자주 쓰이니, import 명령문 외워두자

q_cnt, target_cnt = map(int,sys.stdin.readline().strip().split())
target_location = deque(map(int,sys.stdin.readline().strip().split())) # 이렇게 바로 생성하면서 deque 형태로 만들어둘 수 있다! 리스트형태로 만들고 다시 덱으로 변환하는 것은 줄낭비
q = deque([i+1 for i in range(q_cnt)])
cnt = 0

while target_location:
    if target_location[0] == q[0]:
        target_location.popleft()
        q.popleft()
    
    elif target_location[0] != q[0]:
        if q.index(target_location[0]) <= len(q)//2:
            q.append(q.popleft())
            cnt += 1
        elif q.index(target_location[0]) > len(q)//2:
            q.appendleft(q.pop())
            cnt += 1

print(cnt)