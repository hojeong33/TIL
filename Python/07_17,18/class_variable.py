#클래스 변수 - 클래스 내에서 클래스명.변수 형식으로 선언된 변수
class Person:
    count=0

    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        Person.count+=1
        print("{0}객체가 생성".format(self.__name))

    def __del__(self):
        print("{0}객체가 제거".format(self.__name))

    def to_str(self):
        return('{0}{1}'.format(self.__name,self.__age))

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age<0:
            raise TypeError("나이는 0이상의 값만 허용")
        self.__age=age

people=[
    Person('전호정',24),
    Person('전성준',20)
    ]

print("햔제 Person 클래스의 인스턴스는 총{0}개입니다.".format(Person.count))
