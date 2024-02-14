'''스택 개념 및 구현'''
# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0     # 0이면 True, 0이 아니면 False
    
#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print("스택이 비어있습니다.")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]   # 비어있지 않다면 맨뒤 인자 출력
#         else:
#             print("스택이 비어있습니다.")

#     def size(self):
#         return len(self.items)
    
# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)

# print("스택의 크기:", stack.size())  # 출력: 3
# print("가장 위의 항목:", stack.peek())  # 출력: 3

# print("Pop된 항목:", stack.pop())  # 출력: 3
# print("가장 위의 항목:", stack.peek())  # 출력: 2
# print("스택이 비어있는가?", stack.is_empty())  # 출력: False

# print("Pop된 항목:", stack.pop())  # 출력: 2
# print("Pop된 항목:", stack.pop())  # 출력: 1
# print("스택이 비어있는가?", stack.is_empty())  # 출력: True
# print("Pop된 항목:", stack.pop())  # 출력: "스택이 비어있습니다."



'''스택의 응용(괄호 검사)'''
# def is_balanced(expression):
#     stack = []
#     opening_brackets = "({["
#     closing_brackets = ")}]"
#     brackets_map = {')':'(', '}':'{', ']':'['}

#     for char in expression:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if not stack:   # 만약 비어있다면
#                 return False
#             elif stack[-1] == brackets_map[char]:   # 맨 마지막 인자가 입력값과 키와 밸류가 일치할 때
#                 stack.pop()
#             else:
#                 return False

#     return len(stack) == 0  # 전부 pop을 통해 제거됐다면 True, 아니면 False

# print(is_balanced("((()))"))   # 출력: True
# print(is_balanced("{[()]}"))   # 출력: True
# print(is_balanced("((()"))    # 출력: False
# print(is_balanced("{{{{"))    # 출력: False
# print(is_balanced(")}"))      # 출력: False  



'''스택의 응용(미로 탐색)'''
# def is_valid_move(maze, row, col):
#     if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] == 0:
#         return False
#     return True

# def dfs_maze(maze, start, end):
#     stack = [start]  
#     visited = set()

#     while stack:    # stack 에 값이 존재한다면
#         current_row, current_col = stack.pop()  # 현재의 위치를 각각 저장

#         if (current_row, current_col) == end:
#             return True
        
#         if (current_row, current_col) not in visited:   # 방문하지 않았다면
#             visited.add((current_row, current_col))     # 방문한 장소 저장

#             # 상하좌우 이동
#             directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#             for dr, dc in directions:
#                 new_row, new_col = current_row + dr, current_col + dc
#                 if is_valid_move(maze, new_row, new_col):
#                     stack.append((new_row, new_col))    # 모든 경우를 스택에 저장하여 나중에 사용

#     return False     

        
# maze = [
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [0, 0, 0, 1, 1],
#     [1, 0, 1, 1, 0],
#     [1, 1, 1, 1, 1]
# ]
# start = (4, 1)
# end = (3, 0)

# if dfs_maze(maze, start, end):
#     print("도착점에 도달 가능합니다.")
# else:
#     print("도착점에 도달할 수 없습니다.")



'''큐의 이해와 구현'''
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.items = deque()    # deque를 사용하여 큐 초기화
#         # 데크에서는 인자를 제거하고 이동시킬 필요가 없음

#     def is_empty(self):
#         return len(self.items) == 0
    
#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.popleft()     # 맨 왼쪽 인자 제거
#         else:
#             print("큐가 비어있습니다.")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         else:
#             print("큐가 비어있습니다.")

#     def size(self):
#         return len(self.items)
    
# queue = Queue()

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print("스택의 크기:", queue.size())
# print("가장 위의 항목:", queue.peek())

# print("Pop된 항목:", queue.dequeue())  # 출력: 1
# print("가장 위의 항목:", queue.peek())  # 출력: 2
# print("스택이 비어있는가?", queue.is_empty())  # 출력: False

# print("Pop된 항목:", queue.dequeue())  # 출력: 2
# print("Pop된 항목:", queue.dequeue())  # 출력: 3
# print("스택이 비어있는가?", queue.is_empty())  # 출력: True
# print("Pop된 항목:", queue.dequeue())  # 출력: "큐가 비어있습니다."
