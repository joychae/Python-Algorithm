import sys

N = int(sys.stdin.readline().strip())
data_list = [list(sys.stdin.readline().strip()) for _ in range(N)]

def divide(x, y, n): # x행, y열
    data_type = data_list[x][y]

    data_result = []
    for i in range(x,x+n):
        for j in range(y,y+n):
            if data_type != data_list[i][j]:
                data_result.append('(')
                data_result.extend(divide(x, y, n//2))
                data_result.extend(divide(x, y+(n//2), n//2))
                data_result.extend(divide(x+(n//2), y, n//2))
                data_result.extend(divide(x+(n//2), y+(n//2), n//2))
                data_result.append(')')
                return data_result
    
    return str(data_list[x][y])

print(''.join(divide(0, 0, N)))
