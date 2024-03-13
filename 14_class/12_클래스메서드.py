#클래스 메서드(class method)
#   - 인스턴스를 통하지 않고 클래스에서 바로 호출
#   - @classmethod를 지정하여 사용

class Person:
    count = 0 #클래스 변수로 사용

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls): #cls : 클래스를 의미
        print(f'{cls.count}명 태어났어요')

    def create(selfcls): #생성자와 같은 메서드
            p = cls() #Person()
            return p

kim = Person()
Person.print_count() #결과: 1명 태어났어요

choi = Person()
Person.print_count() #결과: 2명 태어났어요

lee = Person() #클래스 메서드로 인스턴스 생성
Person.print_count() #결과: 3명 태어났어요
