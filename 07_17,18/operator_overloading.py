#연산자 오버로딩 - 연산자에 매핑된 메서드가 없음, 연산자를 중복해서 정의
class Person:
    count=0

    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        Person.count+=1
        print("{0} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return '{0}{1}'.format(self.__name,self.__age)

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age <0:
            raise TypeError("나이는 0이상")
        self.__age=age
    
    @classmethod
    def get_info(cls): #클래스 참조 정보가 인자로 넘어올 매개변수
        return "현재 Person 클래스의 인스턴스는 총 {0}개입니다.".format(cls.count) #=Person.count
    
    def __gt__(self,other):
        return self.__age>other.__age 
    
    def __ge__(self,other):
        return self.age>=other.__age

    def __lt__(self,other):
        return self.age<other.__age

    def __le__(self,other):
        return self.__age<=other.__age

    def __eq__(self,otehr):
        return self.__age==otehr.__age

    def __ne__(self,other):
        return self.__age!=other.__age


members=[
    Person("전호정",24),
    Person("전성준",20),
    Person("전준혁",27)
]

cnt=len(members)
i=0
while True:
    print("members[{0}]>members[{1}]=>{2}".format(i,i+1,members[i]>members[i+1]))
    i+=1
    if i==cnt-1:
        print("members[{0}]>members[{1}]=>{2}".format(i,0,members[i]>members[0]))
        break

print(Person.get_info())