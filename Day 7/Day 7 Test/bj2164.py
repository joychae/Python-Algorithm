import sys
import collections

N = int(sys.stdin.readline().strip())
q = collections.deque([i+1 for i in range(N)])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])


# import sys
# import collections

# N = int(sys.stdin.readline().strip())
# q = collections.deque([i+1 for i in range(N)])
# q.reverse()

# while True:
#     q.pop()
#     if len(q) == 1:
#         print(q[0])
#         break
#     else:
#         delete = q[-1]
#         q.pop()
#         q.appendleft(delete)