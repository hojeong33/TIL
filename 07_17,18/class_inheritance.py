#클래스 상속 #부모(멤버가 상속되는) -> 자식(멤버를 상속하는 ) 단일 상속만
class Parent:
    def __init__(self,family_name):
        self.__family_name=family_name
        print("Parent 클래스의 __init__()...")

    @property
    def family_name(self):
        return self.__family_name

class Child(Parent):
    def __init__(self,first_name,last_name):
        Parent.__init__(self,last_name) #부모클래스 생성 재정의
        # super().__init(last_name)
        self.__first_name=first_name
        print("Child 클래스의 __init__()...")
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self,first_name):
        self.__first_name=first_name
    
    @property
    def name(self):
        return "{0} {1}".format(self.family_name,self.first_name)
        