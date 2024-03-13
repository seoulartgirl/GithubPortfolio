#다중상속: 여러 클래스에서 상속받음
class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
    def greeting(self):
        print(f'{self.name}: 안녕하세요.')

class Student(Person): #상속받음
    def __init__(self, name='', age=0, stuid=''):
        super().__init__(name, age)
        self.stuid = stuid

    def study(self):
        print(f'{self.name}이 공부하기')

class University:
    def __init__(self, department='', grade=''):
        self.department = department
        self.grade = grade

    def manageScore(self):
        print(f'{self.department}에서 공부하기')

class Undergraduate(Student, University):
    pass

lee = Person(name='lee')
kim = Student(name='kim')
lee.greeting() #결과: lee: 안녕하세요.
kim.greeting() #결과: kim: 안녕하세요.
kim.study() #결과: kim이 공부하기
choi = Undergraduate(name='choi')
choi.study() #결과: choi이 공부하기 / 다중상속
