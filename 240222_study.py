'''연결된 구조(단순 연결 리스트)'''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None    # next 초기화

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head     # head 노드 기준으로 순회
#             while current.next:     # 현재 노드의 다음이 비어있다면 멈춤
#                 current = current.next
#             current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=' -> ')
#             current = current.next
#         print('None')
    
# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)

# my_list.display()



'''연결된 구조(이중 연결 리스트)'''
# 이중 연결 리스트는 역방향으로 노드를 탐색, 삽입, 삭제할 수 있다는 점에서 용이하다
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current     # 상호적으로 연결

#     def display(self):
#          current = self.head
#          while current:
#              print(current.data, end=' <-> ')
#              current = current.next
#          print('None')
    
# # 예시 리스트 생성
# my_doubly_list = DoublyLinkedList()
# my_doubly_list.append(1)
# my_doubly_list.append(2)
# my_doubly_list.append(3)

# # 리스트 출력
# my_doubly_list.display()



'''연결된 구조(원형 연결 리스트)'''
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head   # tail과 head 연결

    def display(self):
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print("...")
        
# 예시 리스트 생성
my_circular_list = CircularLinkedList()
my_circular_list.append(1)
my_circular_list.append(2)
my_circular_list.append(3)

# 리스트 출력
my_circular_list.display()
