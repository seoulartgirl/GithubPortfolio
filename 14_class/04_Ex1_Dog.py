#실습.Dog Class 만들기
class Dog:
    dog_id = 0 #class의 변수 / 전역변수가 됨
    def __init__(self, name='', breed='', size='', age=0, color=''):
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
        Dog.dog_id = self.dog_id + 1 #id가 하나씩 늘어나게 됨

    def eat(self, food):
        print(f'"{self.name}"이/가 "{food}"를 먹는다')

    def sleep(self):
        print(f'"{self.name}"이/가 잠잔다')

    def sit(self):
        print(f'"{self.name}"이/가 앉아있다')

    def run(self):
        print(f'"{self.name}"이/가 뛴다')

    def __repr__(self): #문자열로 출력해줌
        return f'{self.name}의 품종은 {self.breed}, 나이는 {self.age}'

dog1 = Dog('삐삐', 'Maltese', 'small', 2, 'white')
print(dog1.dog_id) #결과: 1
dog2 = Dog('벤', 'Chow Chow', 'medium', 3, 'brown')
print(dog2.dog_id) #결과: 2
dog3 = Dog('뭉치', 'Mastiff', 'large', 5, 'black')
print(dog3.dog_id) #결과: 3

dog1.eat('rice') #결과: "삐삐"이/가 "rice"를 먹는다
dog2.sleep() #결과: "벤"이/가 잠잔다
dog3.sit() #결과: "뭉치"이/가 앉아있다
dog1.run() #결과: "삐삐"이/가 뛴다

print(dog1) #결과: 삐삐의 품종은 Maltese, 나이는 2
print(dog2) #벤의 품종은 Chow Chow, 나이는 3

print(dog1.breed) #결과: Maltese
dog4 = Dog()
print(dog4.dog_id) #결과: 4

# 인스턴스 변수: 인스턴스가 소유하고 있는 변수
# 클래스 변수: 전역변수와 같이 클래스의 모든 인스턴스들이 공유하는 변수
#   클래스이름.클래스변수명으로 메서드 내부에서 사용하고
#   인스턴스이름.클래스변수명으로 사용

