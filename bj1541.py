# 잃어버린 괄호(그리디 알고리즘 연습)
# 맞은 문제

import sys

equation = sys.stdin.readline().strip()
equation_numbers = equation.split("-")
first_number = equation_numbers.pop(0)
if "+" in first_number:
    first_number = first_number.split("+")
    first_number = [int(i) for i in first_number]
    first_number = sum(first_number)
else:
    first_number = int(first_number)

first_calculate_num = []
second_calculate_num = []

for num in equation_numbers:
    if "+" in num:
        plus_num = num.split("+")
        plus_num = [int(i) for i in plus_num]
        first_calculate_num.append(plus_num)
        continue
    list_transtion = []
    list_transtion.append(int(num))
    first_calculate_num.append(list_transtion)

for i in first_calculate_num:
    second_calculate_num.append(sum(i))

result = first_number - sum(second_calculate_num)

print(result)

# 진수님 코드

expression = input().split('-')
result = 0 

for i in map(int,expression[0].split('+')):
    result += i

for i in expression[1:]:
    for j in i.split("+"):
        result -= int(j)      
print(result)


