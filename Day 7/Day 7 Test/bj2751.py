import sys

case = int(sys.stdin.readline().strip())

arr = []
for _ in range(case):
    input = int(sys.stdin.readline().strip())
    arr.append(input)

arr =  sorted(arr)

for i in arr:
    print(i)
