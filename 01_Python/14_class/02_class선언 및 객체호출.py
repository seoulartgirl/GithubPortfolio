#*참고: 파이썬의 클래스들: int, float, str, set, dict, list, tuple, ...
a = int(10)
print(a) #결과: 10
b = list(range(10))
print(b) #결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = dict(x=10, y=20)
print(c) #결과: {'x': 10, 'y': 20}

print(type(a), type(b), type(c))
#결과: <class 'int'> <class 'list'> <class 'dict'>
print(isinstance(a, int)) #결과: True
print(isinstance(a, float)) #결과: False
d = 10.5
print(isinstance(d, float)) #결과: True


# 클래스 선언
# class 클래스이름[(상속클래스)]:
#       클래스변수(필드) 선언
#       메서드 정의
#       def 메서드이름(self, 매개변수들):
#           문장들

# 객체(인스턴스) 생성
# 이름 = 클래스명() : 생성자
# 객체: 단독으로 객체만 지칭 / 객체 = 인스턴스
# 인스턴스(instance) : 클래스와 연관지어 부를때


#예. 자동차 클래스 선언
#필드(변수)
#메서드 정의
#self : 기존의 함수와 구분, 자신의 객체(인스턴스)임을 의미
class Car:
    pass

car1 = Car() #car() : 인스턴스 생성하는 생성자 함수 (메소드)
car2 = Car()
car3 = Car()

print(type(car1), id(car1)) #결과: <class '__main__.Car'> 4379630944
print(type(car2), id(car2)) #결과: <class '__main__.Car'> 4379630800
print(type(car3), id(car3)) #결과: <class '__main__.Car'> 4379630848

class Car:
    color = ''
    speed = 0
    def drive(self):
        self.speed = 10


#인스턴스 생성
car1 = Car() #Car() : 인스턴스 생성하는 생성자 함수 (메소드)
car2 = Car()
car3 = Car()

#인스턴스의 필드 이용: 인스턴스이름.필드명
print(type(car1), id(car1))
print(type(car2), id(car2))
print(type(car3), id(car3))

print(car1.speed) #결과: 0
print(car2.speed) #결과: 0
print(car3.speed) #결과: 0


#isinstance(인스턴스명, 클래스명) : 특정 클래스의 인스턴스인지 확인
print(isinstance(car1, Car))
#결과: True / 인스턴스 인지 확인하는 함수

print(f'car1의 speed {car1.speed}')
print(f'car2의 speed {car2.speed}')
print(f'car3의 speed {car3.speed}')


#인스턴스 생성 후 필드 추가하고 값을 대입할 수 있음
#효율적이진 못한 코드
car1.color = 'red'
car2.color = 'blue'
car3.color = 'yellow'
car1.speed = 0
car1.speed = 0
car1.speed = 0
print(car1.color) #결과: red


# 메서드 호출: 인스턴스이름.메서드명(인수들)
car1.drive()
print(car1.speed) #결과: 10
# print(car2.speed)
# print(car3.speed)
