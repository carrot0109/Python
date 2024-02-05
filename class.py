'''2차원 게임 : 미로'''
# import tkinter
# import tkinter.messagebox

# key = ''
# def key_down(e):
#     global key
#     key = e.keysym  # 누른 키 이름(명칭으로)을 key에 대입

# def key_up(e):
#     global key
#     key = ''

# mx = 1  # 캐릭터 가로 방향 위치를 관리하는 변수
# my = 1  # 캐릭터 세로 방향 위치를 관리하는 변수
# yuka = 0    # 칠한 횟수 저장 변수

# def main_proc():
#     global mx, my, yuka
#     if key == 'Shift_L' and yuka > 1:
#         canvas.delete('PAINT')  # 분홍색 지역을 제거
#         mx = 1
#         my = 1  # mx, my에 1을 대입함으로써 초기화
#         yuka = 0
#         for y in range(7):
#             for x in range(10):
#                 if maze[y][x] == 2:
#                     maze[y][x] = 0

#     if key == 'Up' and maze[my - 1][mx] == 0:
#         my = my - 1
#     if key == 'Down' and maze[my + 1][mx] == 0:
#         my = my + 1
#     if key == 'Left' and maze[my][mx - 1] == 0:
#         mx = mx - 1
#     if key == 'Right' and maze[my][mx + 1] == 0:
#         mx = mx + 1
#     if maze[my][mx] == 0:
#         maze[my][mx] = 2    # 한 붓 그리기 형식
#         yuka += 1   
#         canvas.create_rectangle(mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill='pink', width=0, tag='PAINT') 

#     canvas.delete('MYCHR')      # 캐릭터가 핑크색으로 덮이기 때문에 '위치 이동' 대신 '제거' 후 '생성' 사용
#     canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag='MYCHR')
#     # canvas.coords('MYCHR', mx * 80 + 40, my * 80 + 40)  # 캐릭터를 중앙을 기점으로 옮기기 위해 40을 기준으로 이동

#     if yuka == 30:
#         canvas.update()     # 캔버스 업데이트
#         tkinter.messagebox.showinfo('축하합니다!','모든 바닥을 칠했습니다!')    # 클리어 메세지 표시
#     else:
#         root.after(100,main_proc)   # 클리어를 하지 못했다면 다시 실행

# root = tkinter.Tk()
# root.title('미로 색칠')
# root.bind('<KeyPress>',key_down)
# root.bind('<KeyRelease>',key_up)
# canvas = tkinter.Canvas(width=800, height=560, bg='white')
# canvas.pack()
# maze = [
#     [1,1,1,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,1,0,0,1],
#     [1,0,1,1,0,0,1,0,0,1],
#     [1,0,0,1,0,0,0,0,0,1],
#     [1,0,0,1,1,1,1,1,0,1],
#     [1,0,0,0,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1,1,1,1]
# ]
# for y in range(7):
#     for x in range(10):
#         if maze[y][x] == 1:
#             canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill='gray', width=0)  # 두 점의 위치를 지정하여 사각형 생성
#             # 블럭사이 구분을 위해 크기를 79로 설정

# img = tkinter.PhotoImage(file='mimi_s.png')
# canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag='MYCHR')
# main_proc()
# root.mainloop()


'''pygame'''
import pygame
import sys

WHITE = (255, 255, 255)     # 색 정의(하양)
BLACK = (0, 0, 0)   # 색 정의(검정)

def main():
    pygame.init()   # 모듈 초기화
    pygame.display.set_caption('첫 번째 Pygmae')    # 윈도우에 표시할 타이틀 지정
    screen = pygame.display.set_mode((800, 600))    # 그릴 화면(스크린) 초기화
    clock = pygame.time.Clock()     # clock 오브젝트 초기화
    font = pygame.font.Font(None, 80)   # font오브젝트 초기화
    tmr = 0     # 시간 관리 변수

    while True:
        tmr += 1
        for event in pygame.event.get():    # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT:   # 에러 없이 창 닫기
                pygame.quit()
                sys.exit()

        txt = font.render(str(tmr), True, WHITE)    # surface 에 문자열 표시
        screen.fill(BLACK)  # 스크린 전체 채움
        screen.blit(txt, [300, 200])    # 문자열 표시한 surface 를 스크린으로 전송
        pygame.display.update()
        clock.tick(10)  # 딜레이 설정

if __name__ == '__main__':  # 프로그램 직접 실행
    main()