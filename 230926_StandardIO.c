'''표준 입출력'''

print("python", "java",sep=" vs ", end="?")     # end -> 문장의 끝 부분을 변경 (지금까지는 줄바꿈으로 되어있었음)
print("무엇이 더 재밌을까요?")

import sys
print("python","java",file=sys.stdout)  # 표준 출력
print("python","java",file=sys.stderr)  # 표준 에러 처리

scores = {"수학":0, "영어":50,"코딩":100}
for subject, score in scores.items():   # items --> key and value
    print(subject.ljust(4), str(score).rjust(4),sep=":")    # ljust(n) : n칸을 확보하고 왼쪽 정렬

# 은행 대기순번표
# 001 002 003 ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))    # zfill(n) : n만큼의 공간을 확보하고 빈공간은 0으로 채움

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
# input을 통해 숫자를 입력하든 문자를 입력하든 출력시 오류가 나지 않는 이유는 항상 문자열 형태로 입력받기 때문
