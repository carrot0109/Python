# '''목표 지점 도달 여부 판정하기'''
# import random

# class game:
#     def __init__(self,name):
#         self.name = name
#         self.pos = 1
#         self.cr = self.name[0].upper()

#     def board(self):
#         print('●' * (self.pos - 1) + self.cr + '●' * (30 - self.pos) + 'Goal')

#     def judge(self):
#         if self.pos > 30:
#             self.pos = 30

#         if self.pos == 30:
#             print(self.name + '님이 승리했습니다!')
#             return 0

#     def move(self):
#         input('Enter를 누르면' + self.name +'님의 말이 움직입니다.')
#         self.pos += random.randint(1,6)

# player = list(map(str,input().split()))

# games = []

# for i in player :
#     games.append(game(i))

# while True:
#     for i in games:
#         i.board()
#         i.move()
#         end = i.judge()
#         if end == 0:
#             break
    
#     for i in games:
#         i.board()
#     print('================================')

#     if end == 0:
#             break

'''GUI'''
'''버튼 배치하기'''
# import tkinter      # 모듈 임포트
# root = tkinter.Tk()     # 윈도우 객체 생성
# root.title('첫 번째 버튼')
# root.geometry('800x600')    # 크기 지정
# button = tkinter.Button(root, text='버튼 문자열', font=('Times NewRoman',24))
# button.place(x=100, y=100)
# root.mainloop()   # 윈도우 표시


'''버튼 클릭 시 반응'''
# import tkinter

# def click_btn():
#     button['text'] = '클릭했습니다.'

# root = tkinter.Tk()
# root.title('첫 번째 버튼')
# root.geometry('700x600')
# button = tkinter.Button(root, text='클릭하십시오', font=('Times New Roman',24), command=click_btn)  # command=함수 --> 클릭시 동작할 함수 지정
# button.place(x=200, y=100)
# root.mainloop()


'''GUI 배치 : 버튼 클릭 반응'''
import tkinter
import random

def click_btn():
    label['text'] = random.choice(['대길','중길','소길','흉'])
    label.update()

root = tkinter.Tk()
root.title('제비뽑기 프로그램')
root.resizable(False,False)     # 창의 크기 조정 (불가능,불가능)
canvas = tkinter.Canvas(root, width=850, height=700)    # 캔버스 컴포넌트 생성
canvas.pack()   # 캔버스 배치
gazou = tkinter.PhotoImage(file="neko_bg.png")  # gazou에 이미지 파일 로드
canvas.create_image(400,300,image=gazou)    # 캔버스에 이미지 그리기
label = tkinter.Label(root,text='??',font=('Times New Roman',120),bg='white')   # 라벨 컴포넌트 생성
label.place(x=380, y=60)
button = tkinter.Button(root, text='제비뽑기',font=('Times New Roman',36),command=click_btn,fg='skyblue')
button.place(x=360,y=400)
button.mainloop()
