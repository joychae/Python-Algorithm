# 큐2 (큐, 덱 연습)
# 맞은 문제 (pypy로 돌렸을 떄만 맞음 효율화 필요)
# 스택 문제는 동일 로직으로 맞았는데 왜그럴까?

import sys
from collections import deque

case = int(sys.stdin.readline().strip())

q = deque()

# 만들어놓은 함수식을 command 명령어 읽어내서 대입하기
for i in range(case):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        q.append(int(command[1]))
    
    elif command[0] == "pop":

        if q:
            result = q[0]
            q.popleft()
            print(result)

        else:
            print(-1)
    
    elif command[0] == "size":
        print(len(q))
    
    elif command[0] == "empty":

        if q:
            print(0)
        
        else:
            print(1)
    
    elif command[0] == "front":

        if q:
            result = q[0]
            print(result)
        
        else:
            print(-1)
    
    elif command[0] == "back":

        if q:
            result = q[-1]
            print(result)
        
        else:
            print(-1)