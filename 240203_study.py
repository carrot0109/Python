'''진단 게임'''
# import tkinter

# KEKKA = [
#     '전생에 고양이었을 가능성은 매우 낮습니다.',
#     '보통 사람입니다.',
#     '특별히 이상한 곳은 없습니다.',
#     '꽤 고양이다운 구석이 있습니다.',
#     '고양이와 비슷한 성격 같습니다.',
#     '고양이와 근접한 성격입니다.',
#     '전생에 고양이었을지도 모릅니다.',
#     '겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다.'
# ]

# def click_btn():
#     pts = 0
#     for i in range(7):
#         if bvar[i].get() == True:
#             pts += 1
#     nekodo = int(100 * pts / 7)     # 고양이 지수 계산. 소수점은 버림
#     text.delete('1.0', tkinter.END)     # 입력 필드 문자열 삭제
#     text.insert('1.0','<진단결과>\n당신의 고양이 지수는 ' + str(nekodo) + '%입니다.\n' + KEKKA[pts])    # 입력 필드에 숫자값 대입

# root = tkinter.Tk()
# root.title('고양이 지수 진단 게임')
# root.resizable(False,False)     # 윈도우 크기 고정
# canvas = tkinter.Canvas(root,width=800, height=600)     # 캔버스 컴포넌트 생성
# canvas.pack()
# gazou = tkinter.PhotoImage(file='mina.png')     # 이미지 로딩
# canvas.create_image(400, 300, image=gazou)      # 이미지 표시
# button = tkinter.Button(text='진단하기', font=('Times New Roman',32), bg='lightgreen', command=click_btn)
# button.place(x=400, y=480) 
# text = tkinter.Text(width=40, height=5, font=('Times New Roman',16))    # 텍스트 입력 필드 컴포넌트 생성
# text.place(x=320, y=30)     # 텍스트 입력 필드 컴포넌트 배치

# bvar = [None] * 7   # BooleanVal 객체용 리스트
# cbtn = [None] * 7     # 체크 버튼용 리스트
# ITEM = [
#     '높은 곳이 좋다',
#     '공을 보면 굴리고 싶어진다',
#     '깜짝 놀라면 털이 곤두선다',
#     '쥐구멍이 마음에 든다',
#     '개에게 적대감을 느낀다',
#     '생선 뼈를 발라 먹고 싶다',
#     '밤, 기운이 난다'
# ]
# for i in range(7):  # 반복해서 체크 버튼 배치
#     bvar[i] = tkinter.BooleanVar()  # BooleanVar 객체 생성
#     bvar[i].set(False)  # 초기값 설정
#     cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=('Times New Roman',12), variable=bvar[i], bg='#dfe')   # 체크 버튼 생성
#     cbtn[i].place(x=400, y=160 + 40 * i)    # 체크 버튼 배치
# root.mainloop()


'''실시간 처리 구현'''
# import tkinter

# tmr = 0     # type : int 
# def count_up():
#     global tmr
#     tmr = tmr + 1
#     label['text'] = tmr
#     root.after(1000, count_up)  # 1초 후 다시 이 함수 실행

# root = tkinter.Tk()
# label = tkinter.Label(font=('Times New Roman', 80))
# label.pack()
# root.after(1000, count_up)  # 1초 후 지정한 함수 호출
# root.mainloop()


'''키 입력 받기'''
# import tkinter
# key = 0
# def key_down(e):
#     global key                                                                                                 
#     key = e.keycode   # 아스키코드
#     print('KEY:' + str(key))

# root = tkinter.Tk()
# root.title('키 코드 얻기')
# root.bind('<KeyPress>',key_down)    # bind() 명령으로 키를 눌렀을 때 실행할 함수 지정
# root.mainloop()


'''실시간 캐릭터 움직이기'''
import tkinter


def key_down(e):
    global key
    key = e.keysym  # 눌러진 키 이름을 변수에 저장

def key_up(e):
    global key
    key = ''

def main_proc():
    global cx, cy
    if key == 'Up':
        cy -= 20
    if key == 'Down':
        cy += 20
    if key == 'Left':
        cx -= 20
    if key == 'Right':
        cx += 20
    canvas.coords("MYCHR",cx, cy)   # 캐릭터 이미지를 새로운 위치로 이동
    root.after(100, main_proc)

key = ''

cx = 400
cy = 300

root = tkinter.Tk()
root.title("캐릭터 이동")
root.bind('<KeyPress>', key_down)   # 키를 눌렀을 때 실행할 함수 지정
root.bind('<KeyRelease>',key_up)    # 키를 눌렀다 뗐을 때 실행할 함수 지정
canvas = tkinter.Canvas(width=800, height=600, bg='lightgreen')
canvas.pack()
img = tkinter.PhotoImage(file='mimi.png')
canvas.create_image(cx, cy, image=img, tag="MYCHR")
main_proc()
root.mainloop()
