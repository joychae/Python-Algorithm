# 나무 자르기(이분탐색)
# 1회차 틀린 문제 / 2회차 틀린 문제 528ms
# 1회차 - while문 밖에 그릇들 만들고 적재적소에 넣어서 결과값 뽑는 부분이 미숙, 로직은 맞음
# 2회차 - 1) tree_get 값을 while문 밖에다가 생성하여 while문 돌면서 초기화를 안시키는 실수를 함
# 2회차 - 2) mid_height 값을 while문 밖에다가 생성하여 while문 돌면서 초기화를 안시키는 실수를 함
# 2회차 - 3) ans를 elif 세번째 조건에도 넣어 틀렸습니다를 받음 이 로직에 대해서는 아직 이해를 다 하지 못하였음

import sys

tree_cnt, tree_required = map(int,sys.stdin.readline().strip().split())
tree_height = list(map(int, sys.stdin.readline().strip().split()))
min_height = 0
max_height = max(tree_height)
ans = 0

while min_height <= max_height:
    mid_height = (min_height + max_height) // 2 #while문 돌면서 초기화 되고, 재설정 되어야 하는 값은 while문 안에 잘 넣어주자
    tree_get = 0

    for tree in tree_height:
        if tree > mid_height:
            tree_get += tree - mid_height

    if tree_get == tree_required: # 같을 때를 따로 생각해서 바로 break을 걸어주니 >= 일 경우로 묶어서 생각했을 떄보다 1200ms -> 528ms으로 줄어듬
        ans = mid_height
        break
    elif tree_get > tree_required:
        ans = mid_height
        min_height = mid_height + 1
    elif tree_get < tree_required:
        max_height = mid_height - 1

print(ans)