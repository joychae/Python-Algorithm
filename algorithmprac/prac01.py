# # 재귀함수

# def count_down(number):
#     if number < 0 :
#         return
#     print(number)          # number를 출력하고
#     count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


# count_down(60)

# # 재귀함수 연습 (팩토리얼)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

# # 회문검사

# input = "abcba"


# def is_palindrome(string):
#     if string[0] != string[-1]:
#         return False
#     if len(string) <= 1:
#         return True
#     return is_palindrome(string[1:-1])



# print(is_palindrome(input))

# # 버블정렬

# input = [4, 6, 2, 9, 1]

# def bubble_sort(array):
#     n = len(array)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]

#     return

# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!


# # 선택정렬

# input = [4, 6, 2, 9, 1]


# def selection_sort(array):
#     n = len(array)

#     for i in range(n - 1):
#         min_index = i
#         for j in range(n- i):
#             if array[i+j] < array[min_index]:
#                 min_index = i + j
#         array[i],array[min_index] = array[min_index],array[i]
#     # 이 부분을 채워보세요!
#     return

# selection_sort(input)
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

# # 삽입정렬

# input = [4, 6, 2, 9, 1]


# def insertion_sort(array):
#     for :
        
#     # 이 부분을 채워보세요!
#     return


# insertion_sort(input)
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

# 병합정렬

array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    # 이 곳을 채워보세요!
    return array


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!