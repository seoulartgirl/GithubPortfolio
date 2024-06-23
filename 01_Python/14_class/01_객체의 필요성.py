#객체의 필요성

# 더하기 기능을 위한 계산기 구형
# 3 + 4 + 5 + 9

#기존 방식: 16명을 위해 동시에 하려면 16번 실행해야함
# result2 = 0
# def adder2(num):
#     global result2 #global 이라고 지정안해주면 오류남
#     result2 += num
#     return result2
#
# print(adder2(3)) #결과: 3
# print(adder2(7)) #결과: 10
# print(adder2(9)) #결과: 19

#클래스 틀
class AddCal:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

myadder = AddCal() #객체를 만드는 생성자 / 변수
myadder.adder(10)
print(myadder.result) #결과: 10
myadder.adder(20)
print(myadder.result) #결과: 30
myadder.adder(30)
print(myadder.result) #결과: 60

youradd = AddCal() #새 변수 / 결과값 새로 형성
print(youradd.result) #결과: 0
youradd.adder(100)
print(youradd.result) #결과: 100

print(type(myadder)) #<class '__main__.AddCal'> / AddCal 클래스 이름으로 나옴


