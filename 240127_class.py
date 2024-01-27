'''다양성'''
# class Developer:
#     def __init__(self,name):
#         self.name = name

#     def coding(self):
#         print(self.name + ' is developer!!')

# class PythonDeveloper(Developer):
#     def coding(self, tgName = 'Python'):
#         print(self.name + f' is {tgName} developer!!')

# class JavaDeveloper(Developer):
#     def coding(self, tgName = 'Java'):
#         print(self.name + f' is {tgName} developer!!')

# class CPPDeveloper(Developer):
#     def coding(self, tgName = 'C++'):
#         super().coding()    # 부모 인스턴스 coding() 함수 호출
#         print(self.name + f' is {tgName} developer!!')

# pd = PythonDeveloper('Chris')   # 인스턴스 생성
# jd = JavaDeveloper('Jason')
# cd = CPPDeveloper('Bryan')
# pd.coding() # 메서드 호출
# jd.coding()
# cd.coding()


'''모듈 정의 및 불러오기'''
# import fibo
# fibo.fib(20)    # fib함수 호출

# f = fibo.fib    # 함수를 f 변수에 담기
# f(50)

# from fibo import fib, fib2
# fib(500)    # 함수명만으로 함수 호출

# from fibo import fib as f1, fib2 as fib2    # 별칭
# f1(500)

# if __name__ == "__main__":
#     import sys
#     for i in range(len(sys.argv)) :     # 외부에서 인자 받기
#         print(" >> ", sys.argv[i])
#         if len(sys.argv) > 1 and i > 0 :
#             fibo.fib(int(sys.argv[i]))


'''정규식'''
import re
def email_validation_check():
    pass

def password_validation_check(pwd):
    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, '의 길이가 적당하지 않습니다.')
        return False
        
    if re.findall('[a-zA-Z0-9]+', pwd)[0] != pwd:
        print(pwd, '는 숫자와 영문자로만 구성되지 않았습니다.')
        return False
    
    if len(re.findall('[a-z]',pwd)) == 0 or len(re.findall('[A-Z]',pwd)) == 0:
        print(pwd, '는 영문 대문자와 소문자가 함께 존재하지 않습니다.')
        return False
    
    print(pwd, '는 비밀 번호로 적당합니다!!')
    return True

if __name__ == '__main__':
    password_validation_check('23dfe')
    password_validation_check('432fewrf53')
    password_validation_check('2@3flg%')
    password_validation_check('3k39QLe6o0')
