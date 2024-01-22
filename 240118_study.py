'''가변인자'''
# def introduce_your_family(name,*family_names,**family_info):    # * --> 가변인자[여러개의 변수를 저장](튜플 형태로) / ** --> 가변인자(딕셔너리 형태로)
#     print('제 이름은',name,'입니다. ')
#     print('제 가족들의 이름은 아래와 같아요. ')
#     for name in family_names:
#         print(name)
#     print('-'*40)
#     for key in family_info.keys():
#         print(key,":",family_info[key])

# intrduce_your_family('Chris','Jinhee','Anna','Shinhoo',집='용인',가훈='행복하게 살자!')    # 매개변수 순서대로


'''패킹 / 언패킹'''
# print(list(range(3, 6)))
# args = [3, 6]
# print(list(range(*args)))   # 튜플로 인자를 받으면서 3과 6을 언패킹


'''클래스'''
# var = '파이썬 객체 지향 이야기'
# print(id(var)) # 식별하는 정도의 개념 
# print(type(var))

# var = '5' 
# print(id(var)) # 변수의 id 가 바뀜 (리스트의 경우 id 가 계속 동일)
# print(type(var))

# print(var.__class__)    # __class__ : 클래스 확인
# var2 = var.replace('5','Python')
# print(var.replace('5','Python'))  # var값 일부 변경 (replace()는 값을 변경시켜 반환해주나 원형을 변경시키지는 않음)
# print(var)
# print(var2)

# import testClass as t
# book = t.BookReader()
# book.name = "Human"
# book.read_book()

# book2 = t.BookReader()
# book2.name = "Human2"
# book2.read_book()

class BookReader:
  name = str()
  def read_book(self):
    print(self.name + ' is reading Book!!!')
