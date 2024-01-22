'''생성자 함수'''
# class BookReader:
#     country = 'South Korea'
#     def __init__(self, name):   # 생성자 함수 (무조건 제일 먼저 실행)
#         self.name = name

#     def read_book(self):
#         print(self.name+' is reading Book!!')

# reader1 = BookReader('Chris')
# reader2 = BookReader('Anna')
# print(reader1.country)    # 클래스 변수 country값 확인
# reader1.read_book()   # 함수 호출
# reader2.read_book()


'''클래스 내 공유'''
# class Dog:
#     tricks = []

#     def __init__(self, name):
#         self.name = name
#         # self.tricks = []  # 생성 및 초기화를 해버리기에 공유되지 않음 

#     def add_trick(self,trick):
#         self.tricks.append(trick)

# fido = Dog('Fido')
# buddy = Dog('Buddy')

# fido.add_trick('구르기')

# buddy.add_trick('두 발로 서기')
# buddy.add_trick('죽은 척 하기')

# print(fido.tricks)  # tricks가 공유되는데 리스트만 가능


'''데이터 은닉'''
# print(dir(Dog))     # 내부에 들어있는 객체들을 확인하는 명령문

# Dog.tricks = ["AAAA"]

# print(Dog.tricks)


'''상속'''
# ex1. 상속 X
# class Bookreader:
#     country = 'South Korea'
    
#     def __init__(self,name):
#         self.name = name
    
#     def read_book(self):
#         print(self.name + ' is reading a Book!!')
    
# class DrumPlayer:
#     country = 'South Korea'
    
#     def __init__(self,name):
#         self.name = name
    
#     def play_drum(self):
#         print(self.name + 'is playing Drum!!')

# a = Bookreader('Chris')
# a.read_book()
# print(a.country)

# b = DrumPlayer('Mike')
# b.play_drum()
# print(b.country)


# ex2. 상속 O
# class Human:
#     country = 'South Korea'

#     def __init__(self, name):
#         self.name = name

# class BookReader(Human):    # 상속
#     def read_book(self):
#         print(self.name + ' is reading Book!!')

# class DrumPlayer(Human):
#     def play_drum(self):
#         print(self.name + 'is playing Drum!!')

# student1 = BookReader('Mike')
# student1.read_book()
# print(student1.country)

# student2 = DrumPlayer('Bob')
# student2.play_drum()
# print(student2.country)
# 만약 이름이 같은 함수가 있다면 오버라이딩


'''사각형 그리는 클래스'''
import turtle as t
t.shape('turtle')
t.speed(0)

class Draw:
    def __init__(self, string, x, y):
        self.string = string
        self.x = x
        self.y = y

    def draw(self):
        t.up()
        t.goto(self.x,self.y)
        t.down()
        for i in range(self.string):
            t.fd(100)
            t.lt(360/self.string)

class triangle(Draw):
    def __init__(self, x, y, string = 3):
        self.string = string
        self.x = x
        self.y =y

class square(Draw):
    def __init__(self, x,y,string = 4):
        self.string = string
        self.x = x
        self.y =y

class fifth(Draw):
    def __init__(self, x, y, string = 5):
        self.string = string
        self.x = x
        self.y =y

tr = triangle(-300,0) # 인스턴스 생성
tr.draw()

tr1 = square(0,0) # 인스턴스 생성
tr1.draw()

tr2 = fifth(300,0) # 인스턴스 생성
tr2.draw()
# 가장 공통되는 코드인 그리는 코드를 클래스 형성한 후 상속받음
# 상속의 가장 큰 이유 : 코드를 줄이기 위해
