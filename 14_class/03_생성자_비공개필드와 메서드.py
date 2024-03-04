# 생성자(constructor)
# 생성자 형식: def __init__(self, *args):
#                   필드들 초기화
# __메서드명__() : 예약함수 / 미리 지정되어있는 함수

# 비공개 필드와 메서드: 정보은닉(encapsulation)
# __변수명 : 비공개 필드는 클래스 내부에서만 사용
#   비공개 필드는 필드 접근가능한 메서드를 정의하여 이용
# __메서드명() : 비공개 메서드 / 클래스 내부에서만 사용 가능한 메서드
#           비공개메서드를 접근할수 있는 메서드를 구현

class Car:
    def __init__(self):
        self.color = 'black'
        self.speed = 0

    def drive(self):
        self.speed = 10

car1 = Car()
car2 = Car()
print(car1.color) #결과: black
print(car2.color) #결과: black

class Car:
    def __init__(self, color, model, date):
        self.color = color
        self.speed = 0
        self.model = model
        self.__date = date #비공개 필드가 됨

    def drive(self):
        self.speed = 10

    #비공개필드 접근법
    def print_date(self):
        print('제조연월일은', self.__date)


car1 = Car('red', 'BMW', '2024-01-01')
car2 = Car('black', 'Nexo', '2020-01-30')
print(car1.color) #결과: red
print(car2.color) #결과: black
print(car1.model) #결과: BMW
#print(car1.__date) #비공개 필드는 직접 사용 불가
#AttributeError: 'Car' object has no attribute '__date'
car1.print_date() #결과: 제조연월일은 2024-01-01

class Car:
    def __init__(self, color, modelN, date, model='BMW'):
        self.color = color
        self.speed = 0
        self.model = model
        self.modelN = modelN
        self.__date = date #비공개 필드가 됨

    def __modelN(self):
        return self.modelN
    def drive(self):
        self.speed = 10

    #비공개필드 접근법
    def print_date(self):
        print('제조연월일은', self.__date)

    def print_info(self):
        print('자동차번호:', self.__modelN())
        print('자동차색상:', self.color)
        print('자동차모델:', self.model)
        self.print_date()

car1 = Car('red', 'a12345','2024-01-01', 'Benz')
car2 = Car('black', 'a12346', '2020-01-30', 'Nexo')
car3 = Car('black', 'a12349', '2020-01-30')
print(car1.model) #결과: Benz
print(car2.model) #결과: Nexo
print(car3.model) #결과: BMW
# print(car1.__date)  # 비공개 필드는 직접 사용불가
# car1.__modelN() # 비공개 메서드는 직접 사용불가
car1.print_date() #결과: 제조연월일은 2024-01-01

car1.print_info()

#결과:
# 자동차번호: a12345
# 자동차색상: red
# 자동차모델: Benz
# 제조연월일은 2024-01-01


