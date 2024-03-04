#다이아몬드 상속 : 다중 상속의 한 사례

class A:
    def greeting(self):
        print('안녕하세요. A입니다')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다')

class D(B,C):
    pass

obj = D()
obj.greeting() #결과: 안녕하세요. B입니다

#다이아몬드 상속: 서로 다른 클래스에서 동일한 메서드를 상속받는 경우
#메서드를 탐색하는 순서 (Method Resolution Order: MRO)
#왼쪽에서 오른쪽 순서로 메서드 탐색

print(D.mro())
#결과: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#메서드 탐색 순서를 보여줌