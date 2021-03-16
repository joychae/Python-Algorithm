# 스택 구현
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.head = None

#     def push(self, value):
#         # 어떻게 하면 될까요?
#         new_head = Node(value)
#         new_head.next = self.head
#         self.head = new_head
#     # pop 기능 구현
#     def pop(self):
#         # 어떻게 하면 될까요?
#         if self.is_empty():
#             return 'Stack is Empty'
#         delete_head = self.head
#         self.head = self.head.next
#         return delete_head

#     def peek(self):
#         # 어떻게 하면 될까요?
#         if self.is_empty():
#             return 'Stack is Empty'
#         return self.head.data
#         return

#     # isEmpty 기능 구현
#     def is_empty(self):
#         # 어떻게 하면 될까요?
#         return self.head is None

# stack = Stack()
# stack.push(3)
# print(stack.peek())
# stack.push(4)
# print(stack.peek())
# print(stack.pop().data)
# print(stack.peek())
# print(stack.is_empty())
# print(stack.pop().data)
# print(stack.is_empty())

# 스택 연습문제

# top_heights = [6, 9, 5, 7, 4]

# def get_receiver_top_orders(heights):
#     answer = [0]*len(heights)
#     while heights:
#         height = heights.pop()
#         for idx in range(len(heights) -1, 0, -1):
#             if heights[idx] > height:
#                 answer[len(heights)] = idx + 1
#                 break
#     return answer        

# print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!


# # 큐

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def enqueue(self, value):
#         # 어떻게 하면 될까요?
#         return

#     def dequeue(self):
#         # 어떻게 하면 될까요?
#         return

#     def peek(self):
#         # 어떻게 하면 될까요?
#         return

#     def is_empty(self):
#         # 어떻게 하면 될까요?
#         return

# # 해쉬
# # 해쉬를 이용한 딕셔너리 구현 / 출석체크

# all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
# present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# def get_absent_student(all_array, present_array):
#     student_dict = {}
#     for key in all_array:
#         student_dict[key] = True

#     for key in present_array:
#         del student_dict[key]

#     for key in student_dict.keys():
#         return key

# print(get_absent_student(all_students, present_students))

# 힙

# class MaxHeap:
#     def __init__(self):
#         self.items = [None]

#     def insert(self, value):
#         self.items.append(value)
#         cur_index = len(self.items) -1 #마지막 인덱스 값

#         while cur_index > 1 :
#             parent_index = cur_index // 2
#             if self.items[cur_index] > self.items[parent_index]:
#                 self.items[cur_index],self.items[parent_index] = self.items[parent_index],self.items[cur_index]
#                 cur_index = parent_index
#             else:
#                 break
#         return


# max_heap = MaxHeap()
# max_heap.insert(3)
# max_heap.insert(4)
# max_heap.insert(2)
# max_heap.insert(9)
# print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

# # DFS

# # 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }

# visited = []

# def dfs_recursion(adjacent_graph, cur_node, visited_array): # cur_node 시작하는 노드
#     visited_array.append(cur_node)
#     for adjacent_node in adjacent_graph:
#         if adjacent_node not in visited_array: #탈출조건
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)
#     return
# # 재귀함수 통해서는 DFS의 길이가 무한정 깊어지면 에러가 발생할 수 있다!

# dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
# print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!

# 스택으로 DFS 구현하기

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack =[]
    visited =[]

    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node not in visited[current_node]:
            stack.append(adjacent_node)
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!