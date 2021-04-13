# 이진 탐색이란?
# 데이터가 정렬된 배열에서 특정한 값을 찾아내는 알고리즘
# 선형 탐색보다 속도가 빠르고 효율적이다

# 이진 탐색의 기본 구조

# 1) 찾고자 하는 수가 존재한다 -> 이 문제에서는 M개의 정수를 모두 찾아야 하네요!

# 2) 탐색할 배열이 존재한다 -> 상근이가 가지고 있는 숫자 카드 배열에서 탐색이 이루어 지네요!

# 3) 이진 탐색을 구현한 함수가 필요하다

# 4) 이진 탐색을 구현한 함수에 찾고자 하는 수, 탐색할 배열을 넣어 요구 조건에 맞게 결과값을 출력한다


# 문제 

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 
# 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 
# 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
# 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# 예제 입력
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10

# 예제 출력
# 1 0 0 1 1 0 0 1


import sys

array_q = int(sys.stdin.readline().strip())
array_numbers = list(map(int,sys.stdin.readline().strip().split()))
array_numbers = sorted(array_numbers)

target_q = int(sys.stdin.readline().strip())
target_numbers = list(map(int,sys.stdin.readline().strip().split()))

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2
    return False

answer_list = []
for i in range(target_q):
    result = is_existing_target_number_binary(target_numbers[i], array_numbers)
    if result is True:
        ans = 1
        answer_list.append(ans)
    else:
        ans = 0
        answer_list.append(ans)

print(*answer_list)