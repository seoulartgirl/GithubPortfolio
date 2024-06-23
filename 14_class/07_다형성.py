#다형성 예.
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')
        # 상속받은 클래스에서 메서드를 구현하시오

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof Woof!'

class Cow(Animal):
    def talk(self):
        return '음메'

animals = [Cat('Missy'), Cat('Mr.Mistoffelees'), Dog('zion'), Cow('아지')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())

#결과:
# Missy: Meow!
# Mr.Mistoffelees: Meow!
# zion: Woof Woof!
# 아지: 음메