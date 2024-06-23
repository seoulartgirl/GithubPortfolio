#예제. Line 클래스
# https://docs.python.org/ko/3/reference/datamodel.html

#특수 메소드들

class Line(object):
    def __init__(self, length): #생성자
        self.length = length
        print(f'{self.length}길이의 선이 생성되었습니다.')

    # def __del__(self): #소멸자 (객체소멸시 자동으로 호출됨)
    #     print(f'{self.length}길이의 선이 삭제되었습니다')

    def __repr__(self):
        return f'선의길이: {self.length}인 선분'
        # 결과: 선의길이: 20인 선분

    def __str__(self):
        return f'선분 {self.length}' # 선분 20

    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __lt__(self, other): #less than other
        return self.length < other.length

    def __gt__(self, other): #greater than other
        return self.length > other.length

    def __le__(self, other): #less or equal other
        return self.length <= other.length

    def __ge__(self, other): #greater than other
        return self.length >= other.length

    def __eq__(self, other): #equal
        return self.length == other.length

    def __ne__(self, other): #not equal
        return self.length != other.length

line1 = Line(10)
line2 = Line(20)
# del(line1) 이 함수를 안불러도 알아서 삭제됨
print(line1) #10
print(line2) #20
print(line1 + line2) #add함수를 지칭 / 결과: 30
print(line1 - line2) #sub함수를 지칭 / 결과: -10
print(line1 >= line2) #ge함수를 지칭 / 결과: False

if line1 > line2:
    print('선분1이 길어요')
else:
    print('선분2가 길어요') #결과: 선분2가 길어요
