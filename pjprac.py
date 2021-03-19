
# array = [1,5,2,6,3,7,4]
# commands = [[2,5,3],[4,4,1],[1,7,3]]

# answer = []
# for i in range(len(commands)):
#     array = array[commands[i][0]-1:commands[i][1]]
#     array.sort()
#     print(array)
#     answer_each = array[commands[i][2]-1]
#     answer.append(answer_each)

# print(answer)

s = "abcde"
if len(s)%2:
    print(s[len(s)//2])