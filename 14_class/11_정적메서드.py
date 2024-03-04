#정적 메서드(static method)
# : 인스턴트를 통하지 않고 클래스에서 바로 호출하여 사용하는 메서드
# : 순수함수(pure function)
# 메서드 위에 @staticmethod 키워드를 지정하여 정의

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def add(a,b):
        print(a-b)

# myCal = Calc()
# myCal.add(10,20)
Calc.add(10,20) # 위 방법 대신 클래스 이름에서 바로 호출해서 사용
