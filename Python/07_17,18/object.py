# class Person:
#     pass

# member=Person() #생성자 매서드 --- __init__

#클래스 생성자 메서드 정의
# class 클래스명:
#     def __init__(self,매개변수목록):
#클래스 소멸자 매서드 정의
# class 클래스명:
#     def __del__(self): #self 객체 공간을 말함

class Person:
    def __init__(self,name,age):
        self.__name=name #프라이빗 필드
        self.__age=age
        print('{0}객체가 생성됨'.format(self.__name))
    def __del__(self):
        print("{0}객체가 제거됨".format(self.__name))
    def to_str(self):#인스턴스 메서드 정의
        return '{0}{1}'.format(self.__name,self.__age)
    def get_name(self):
        return self.__name #getter매세드만
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age<0:
            raise TypeError("나이는 0이상 값만 허용")
        self.__age=age


members=[
    Person("홍길동",20),
    Person("이순신",40)
]
members[0].set_age(-20)

# print("{0}{1}".format(member.name,member.age))
# print(dir(member))

for member in members:
    print(member.to_str())

