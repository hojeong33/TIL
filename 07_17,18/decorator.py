#데코레이터 (getter, setter대신 사용) -변수 이름과 같은 메서드를 만들어 사용가능
class Person:
    def __init__(self,name,age):
        self.__name=name #프라이빗 필드
        self.__age=age
        print('{0}객체가 생성됨'.format(self.__name))
    def __del__(self):
        print("{0}객체가 제거됨".format(self.__name))
    def to_str(self):#인스턴스 메서드 정의
        return '{0}{1}'.format(self.__name,self.__age)

    @property 
    def name(self):#변수처럼 사용가능(getter역할)
        return self.__name 
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age<0:
            raise TypeError("나이는 0이상 값만 허용")
        self.__age=age


members=[
    Person("홍길동",20),
    Person("이순신",40)
]
members[0].age=22