#1. 파이썬의 클래스와 객체지향 틀린것?
#정답: 4

#2.
#정답: (가): 클래스  (나): 인스턴스

#3.
#정답: 1, 3 다형성, 상속

#4-1.
class IceCream(object):
    def __init__(self, flavor):
        self.flavor = flavor
    def change_flavor(self, new_flavor):
        print('아이스크림을 %s에서 %s로 변경해주세요'%(self.flavor, new_flavor))
        self.flavor = new_flavor
        print('아이스크림 맛을 %s로 변경해드렸어요.' %self.flavor)

ice_cream = IceCream("레인보우 샤베트")
ice_cream.change_flavor("바람과 함께 사라지다")

#결과: 아이스크림을 레인보우 샤베트에서 바람과 함께 사라지다로 변경해주세요
# 아이스크림 맛을 바람과 함께 사라지다로 변경해드렸어요

#4-2.
class Person(object):
    def __init__(self, name):
        self.name = name

    def language(self):
        pass

class Earthling(Person):
    def language(self, language):
        return language

class Groot(Person):
    def language(self, language):
        return "I'm Groot!"

name = ['HongGildong', 'Dr.Strange', 'Groot']
country = ['Korea', 'USA', 'Galaxy']
language = ['Korean', 'English', 'Groot']

for idx, name in enumerate(name):
    if country[idx].upper() != 'GALAXY':
        person = Earthling(name)
        print(person.language(language[idx]))
    else:
        groot = Groot(name)
        print(groot.language(language[idx]))

#결과: Korean / English / I'm Groot!


#4-3.
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, back_number):
        self.back_number = back_number

jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
print('현재 선수의 등번호는:', jinhyun.back_number)
jinhyun.change_back_number(5)
print('현재 선수의 등번호는:', jinhyun.back_number)

#정답:
# 현재 선수의 등번호는: 10
# 현재 선수의 등번호는: 5

#4-4.
class Marvel(object):
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic
    def __str__(self):
        return 'My name is {0} and my weapon is {1}'.format(self.name, self.characteristic)

class Villain(Marvel):
    pass

first_villain = Villain("Thanos", "infinity gauntlet")
print(first_villain)

# 결과: My name is Thanos and my weapon is infinity gauntlet

#4-5.
class Terran(object):
    def __init__(self, mineral):
        self.scv = 4
        self.marine = 0
        self.medic = 0
        self.mineral = mineral #50
    def command(self, SCV = False):
        self.mineral += 8*self.scv #32를 더한 값
        if SCV:
            self.scv += 1   #5
            self.mineral -= 10  #72
    def barrack(self, Marine = False, Medic = False):
        self.mineral += 8*self.scv #40을 더한 값 #112
        if Marine:
            self.marine += 1    #1
            self.mineral -= 15  #97
        if Medic:
            self.medic += 1     #1
            self.mineral -= 25      #72
    def check_source(self):
        print("Mineral: " + str(self.mineral))

User = Terran(50)
User.command(True)
User.barrack(True, True)
User.check_source()

#결과: Mineral: 72


#4-6.
class Score:
    def __init__(self, student):
        tmp = student.split(",")
        self.name = tmp[0]      #john
        self.midterm = int(tmp[1])      #90
        self.final = int(tmp[2])        #90
        self.assignment = int(tmp[3])       #0
        self.score = None
        self.grade = None

    def total_score(self):
        test_score = ((self.midterm + self.final)/2)*0.8 #72
        if self.assignment >= 3:
            assign_score = 20
        elif self.assignment >= 2:
            assign_score = 10
        elif self.assignment >= 1:
            assign_score = 5
        else:
            assign_score = 0
        self.score = test_score + assign_score

    def total_grade(self):
        if self.assignment == 0:
            grade = "F"
        elif self.score >= 90:
            grade = 'A'
        elif self.score >= 70:
            grade = 'B'
        elif self.score >= 60:
            grade = 'C'
        else:
            grade = 'F'
        self.grade = grade
        return grade

student_john = Score("john,90,90,0")
aa = student_john.total_score() # 72
bb = student_john.total_grade() # F
print(aa,bb,student_john.score,student_john.grade)

#결과: None, F, 72, F
# 첫번째 None -> return이 없어서


#5-1.
class Person:
    def __init__(self, name, age, position):
        self.Name = name
        self.Age = age
        self.Position = position
    def show_info(self):
        print('이름: {}'.format(self.Name))
        print('나이: {}'.format(self.Age))
        print('직위: {}'.format(self.Position))
        print("저는 {0} {1}입니다. 나이는 {2}입니다".format(self.Position, self.Name, self.Age))

class Researcher(Person):
    def __init__(self, name, age, position, degree):
        Person.__init__(self, name, age, position)
        self.Degree = degree
    def show_info(self):
        Person.show_info(self)
        print("저는 {} 입니다".format(self.Degree))

if __name__ == '__main__':
    researcher_john = Researcher('John', 22, '연구원', '학사')
    researcher_tedd = Researcher('Tedd', 40, '소장', '박사')
    researcher_john.show_info()
    print("="*50)
    researcher_tedd.show_info()

#(가) 결과
# 이름: John
# 나이: 22
# 직위: 연구원
# 저는 연구원 John 입니다. 나이는 22입니다.
# 저는 학사입니다.
#================= (50개 출력)
# 이름: Tedd
# 나이: 40
# 직위: 소장
# 저는 소장 Tedd 입니다. 나이는 40입니다.
# 저는 박사입니다.

#(나) : 상속


#5-2.
class TV(object):
    def __init__(self, size, year, company):
        self.size = size
        self.year = year
        self.company = company
    def describe(self):
        print(self.company + "에서 만든" + self.year + "년형" + self.size + "인치" + 'TV')

class Laptop(TV):
    def describe(self):
        print(self.company + "에서 만든" + self.year + "년형" + self.size + "인치" + '노트북')

LG_TV = TV("32", '2019', 'LG')
LG_TV.describe()

samsung_microwave = Laptop('15', '2018', 'Samsung')

#(가) 결과: LG에서 만든 2019년형 32인치 TV

#(나) 정답: 상속, 다형성