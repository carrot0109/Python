'''큐의 응용(너비 우선 탐색)'''
# from collections import deque

# def bfs(graph, start):
#     visited = set()  # 방문한 노드를 저장하는 집합
#     queue = deque([start])  # 시작 노드를 큐에 넣음
#     while queue:
#         node = queue.popleft()  # 큐에서 가장 인접한 노드를 하나 꺼냄
#         if node not in visited:
#             print(node)  # 노드를 방문함
#             visited.add(node)  # 방문한 노드를 집합에 추가
#             for neighbor in graph[node]:  # 현재 노드와 인접한 모든 노드를 탐색
#                 if neighbor not in visited:
#                     queue.append(neighbor)  # 인접한 노드를 큐에 추가

# # 그래프 정의 (인접 리스트 형태)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C'],
#     'G': ['C']
# }

# # 그래프의 시각화
# #   A
# #  / \
# # B   C
# # |   | \
# # D   F  G
# # |       
# # E       


# # BFS 실행
# bfs(graph, 'B')



'''덱의 이해와 구현'''
# from collections import deque

# # 덱 생성
# Deque = deque()

# # 덱에 항목 추가
# Deque.append(1)     # 오른쪽 끝에 추가
# Deque.appendleft(2)     # 왼쪽 끝에 추가

# # 덱에서 항목 삭제
# Deque.pop()     # 오른쪽 끝에서 삭제
# Deque.popleft()     # 왼쪽 끝에서 삭제

# # 덱의 길이 확인
# print(len(Deque))

# # 덱 출력
# print(Deque)



'''연결된 구조(단순 연결 리스트)'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)   # 생성한 노드를 new_node에 대입
        if not self.head:   # head 노드가 비어있다면
            self.head = new_node
            return
        last_node = self.head   # 마지막 노드를 찾기 위해 기본값 설정
        while last_node.next:   # last_node의 다음 노드가 None이면 멈춤
            last_node = last_node.next
        last_node.next = new_node   # 찾은 마지막 노드 다음에다 연결

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# 연결 리스트 생성
linked_list = LinkedList()

# 요소 추가
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# 연결 리스트 출력
linked_list.print_list()
