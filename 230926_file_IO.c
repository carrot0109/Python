'''파일 입출력'''

score_file = open("score.txt", "w", encoding="utf8")    # 파일 이름, 목적
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)
score_file.close()

score_file = open("score.txt","a",encoding="utf8")  # "a" : append --> 계속 이어씀
score_file.write("과학 : 80")   # write를 통해 출력할 경우 줄바꿈이 따로 존재하지 않음
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt","r",encoding="utf8")  # "r" : read
print(score_file.read())    # 모두 읽어옴
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(),end="")    # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")   
print(score_file.readline(),end="") 
print(score_file.readline(),end="") 
score_file.close()

# 파일이 총 몇 줄인지 모를 때
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:    # 읽어올 라인이 없다면
        break
    print(line,end="")
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
